import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# 파일 로드
file_path = '출생아수__합계출산율__자연증가_등_20260529172733.xlsx'
df = pd.read_excel(file_path, sheet_name=0)

# 데이터 클랜징
df_clean = df.iloc[:, 1:].copy()
df_clean.index = df.iloc[:, 0]

for col in df_clean.columns:
    df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

# 출생아수 데이터
birth_data = df_clean.iloc[0]

# 년도를 정수로 변환
years = []
for y in birth_data.index:
    try:
        years.append(int(str(y).split()[0]))
    except:
        years.append(y)

# ==================== 라인 그래프 ====================
fig, axes = plt.subplots(2, 1, figsize=(12, 10))
fig.suptitle('Birth Rate and Fertility Rate Analysis in Korea', fontsize=16, fontweight='bold')

# 첫 번째 그래프: 출생아수
ax1 = axes[0]
ax1.plot(years, birth_data.values, marker='o', linewidth=3, markersize=10, 
         color='#2E86AB', label='Birth Count')
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Number of Births', fontsize=12, fontweight='bold')
ax1.set_title('Year-over-Year Birth Count Trend', fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.legend(fontsize=11, loc='best')

# 값 표시
for year, value in zip(years, birth_data.values):
    ax1.text(year, value, f'{value:,.0f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 최대/최소 강조
max_val = birth_data.max()
min_val = birth_data.min()
max_idx = birth_data.idxmax()
min_idx = birth_data.idxmin()
max_year = int(str(max_idx).split()[0]) if isinstance(max_idx, str) else max_idx
min_year = int(str(min_idx).split()[0]) if isinstance(min_idx, str) else min_idx

ax1.scatter([max_year], [max_val], color='red', s=200, zorder=5, marker='*', label='Max')
ax1.scatter([min_year], [min_val], color='blue', s=200, zorder=5, marker='*', label='Min')
ax1.legend(fontsize=11, loc='best')

# 두 번째 그래프: 합계출산율
ax2 = axes[1]
fertility_data = df_clean.iloc[2]  # 합계출산율(출/천명)
ax2.plot(years, fertility_data.values, marker='s', linewidth=3, markersize=10, 
         color='#D62828', label='Fertility Rate')
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Total Fertility Rate (per 1000)', fontsize=12, fontweight='bold')
ax2.set_title('Year-over-Year Total Fertility Rate Trend', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.legend(fontsize=11, loc='best')

# 값 표시
for year, value in zip(years, fertility_data.values):
    ax2.text(year, value, f'{value:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('birth_analysis_graph.png', dpi=300, bbox_inches='tight')
print("✓ Graph saved: birth_analysis_graph.png")

# ==================== 추가 분석 ====================
print("\n" + "=" * 80)
print("분석 결과 요약")
print("=" * 80)

print("\n[출생아수 분석]")
for i, (year, value) in enumerate(zip(years, birth_data.values)):
    if i == 0:
        print(f"{year}년: {value:,.0f}명")
    else:
        prev_val = birth_data.values[i-1]
        change = value - prev_val
        change_pct = (change / prev_val * 100)
        print(f"{year}년: {value:,.0f}명 ({change:+,.0f}명, {change_pct:+.1f}%)")

print(f"\n최고: {birth_data.max():,.0f}명 ({max_year}년)")
print(f"최저: {birth_data.min():,.0f}명 ({min_year}년)")
print(f"평균: {birth_data.mean():,.0f}명")
print(f"총 변화: {birth_data.iloc[-1] - birth_data.iloc[0]:+,.0f}명 ({((birth_data.iloc[-1] - birth_data.iloc[0]) / birth_data.iloc[0] * 100):+.1f}%)")

print("\n[전체 지표]")
print(df_clean)

print("\n✓ 분석 완료!")
