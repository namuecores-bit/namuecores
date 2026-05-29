import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['font.sans-serif'] = ['Malgun Gothic']
plt.rcParams['axes.unicode_minus'] = False

# 파일 로드
file_path = '출생아수__합계출산율__자연증가_등_20260529172733.xlsx'
df = pd.read_excel(file_path, sheet_name=0)

# 데이터 클랜징
df_clean = df.iloc[:, 1:].copy()
df_clean.index = df.iloc[:, 0]

for col in df_clean.columns:
    df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

# 년도
years = []
for y in df_clean.columns:
    try:
        years.append(int(str(y).split()[0]))
    except:
        years.append(y)

# ==================== 다각도 분석 ====================
fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

fig.suptitle('대한민국 출생아수 및 합계출산율 종합 분석', 
             fontsize=16, fontweight='bold')

# 1. 출생아수 트렌드
ax1 = fig.add_subplot(gs[0, 0])
birth_data = df_clean.iloc[0]
ax1.plot(years, birth_data.values, marker='o', linewidth=2.5, markersize=8, color='#2E86AB')
ax1.fill_between(years, birth_data.values, alpha=0.3, color='#2E86AB')
ax1.set_title('출생아수 추이', fontweight='bold', fontsize=11)
ax1.set_ylabel('출생아수 (명)')
ax1.grid(True, alpha=0.3)
for year, value in zip(years, birth_data.values):
    ax1.text(year, value, f'{value:,.0f}', ha='center', va='bottom', fontsize=9)

# 2. 합계출산율 트렌드
ax2 = fig.add_subplot(gs[0, 1])
fertility_data = df_clean.iloc[2]
ax2.plot(years, fertility_data.values, marker='s', linewidth=2.5, markersize=8, color='#D62828')
ax2.fill_between(years, fertility_data.values, alpha=0.3, color='#D62828')
ax2.set_title('합계출산율 추이', fontweight='bold', fontsize=11)
ax2.set_ylabel('합계출산율 (명)')
ax2.grid(True, alpha=0.3)
for year, value in zip(years, fertility_data.values):
    ax2.text(year, value, f'{value:.1f}', ha='center', va='bottom', fontsize=9)

# 3. 년도별 증감 (출생아수)
ax3 = fig.add_subplot(gs[1, 0])
changes = []
for i in range(1, len(birth_data)):
    change = birth_data.iloc[i] - birth_data.iloc[i-1]
    changes.append(change)
colors = ['#06A77D' if x >= 0 else '#D62828' for x in changes]
ax3.bar(years[1:], changes, color=colors, alpha=0.7, width=0.4)
ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
ax3.set_title('전년 대비 출생아수 증감', fontweight='bold', fontsize=11)
ax3.set_ylabel('증감 (명)')
ax3.grid(True, alpha=0.3, axis='y')
for year, change in zip(years[1:], changes):
    ax3.text(year, change, f'{change:+,.0f}', ha='center', 
             va='bottom' if change >= 0 else 'top', fontsize=9)

# 4. 자연증가 현황
ax4 = fig.add_subplot(gs[1, 1])
natural_increase = df_clean.iloc[1]
ax4.plot(years, natural_increase.values, marker='^', linewidth=2.5, markersize=8, 
         color='#F77F00', label='Natural Increase/Decrease')
ax4.fill_between(years, natural_increase.values, alpha=0.3, color='#F77F00')
ax4.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
ax4.set_title('자연증가/감소 추이', fontweight='bold', fontsize=11)
ax4.set_ylabel('자연증가 (명)')
ax4.grid(True, alpha=0.3)
for year, value in zip(years, natural_increase.values):
    ax4.text(year, value, f'{value:,.0f}', ha='center', va='bottom', fontsize=8)

# 5. 출산율(천명당)
ax5 = fig.add_subplot(gs[2, 0])
crude_birth = df_clean.iloc[2]
ax5.plot(years, crude_birth.values, marker='D', linewidth=2.5, markersize=8, color='#6A4C93')
ax5.set_title('조출생률 (천명당)', fontweight='bold', fontsize=11)
ax5.set_ylabel('조출생률')
ax5.grid(True, alpha=0.3)
for year, value in zip(years, crude_birth.values):
    ax5.text(year, value, f'{value:.1f}', ha='center', va='bottom', fontsize=9)

# 6. 전체 지표 비교
ax6 = fig.add_subplot(gs[2, 1])
ax6.axis('off')

# 통계 테이블
summary_text = f"""
요약 통계

출생아수:
  최소: {birth_data.min():,.0f}명 ({birth_data.idxmin()})
  최대: {birth_data.max():,.0f}명 ({birth_data.idxmax()})
  평균: {birth_data.mean():,.0f}명
  변화: {birth_data.iloc[-1] - birth_data.iloc[0]:+,.0f}명 ({((birth_data.iloc[-1] - birth_data.iloc[0]) / birth_data.iloc[0] * 100):+.1f}%)

합계출산율:
  최소: {fertility_data.min():.2f} ({fertility_data.idxmin()})
  최대: {fertility_data.max():.2f} ({fertility_data.idxmax()})
  평균: {fertility_data.mean():.2f}
  변화: {fertility_data.iloc[-1] - fertility_data.iloc[0]:+.2f}

추세: 상승세
"""

ax6.text(0.1, 0.9, summary_text, transform=ax6.transAxes, fontsize=10, 
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.savefig('comprehensive_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Comprehensive analysis graph saved: comprehensive_analysis.png")
plt.show()
