import re
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


def fetch_html(url: str, headers: dict = None, timeout: int = 15) -> str:
    if headers is None:
        headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text


def find_news_tab_url(html: str) -> str | None:
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a', href=True):
        href = a['href']
        if 'where=news' in href:
            if href.startswith('?'):
                return 'https://search.naver.com/search.naver' + href
            return href
    return None


def parse_news_titles(html: str) -> list[str]:
    soup = BeautifulSoup(html, 'html.parser')
    titles = []

    # 현재 네이버 뉴스 검색 결과의 기사 제목은 주로 타이틀 링크 내부에 있습니다.
    for a in soup.select('a[data-heatmap-target=".tit"]'):
        text = a.get_text(separator=' ', strip=True)
        if text and len(text) > 5:
            titles.append(text)

    # fallback: 뉴스 기사 링크 내부 텍스트에서 제목 추출
    if not titles:
        news_url_pattern = re.compile(r'https?://(?:n\.)?news\.naver\.com/.+')
        for a in soup.find_all('a', href=news_url_pattern):
            text = a.get_text(separator=' ', strip=True)
            if text and len(text) > 5:
                titles.append(text)

    # 중복 제거 및 순서 유지
    seen = set()
    unique_titles = []
    for title in titles:
        if title not in seen:
            seen.add(title)
            unique_titles.append(title)
    return unique_titles


def save_titles_to_excel(titles: list[str], filename: str = 'naver_result.xlsx') -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = 'Naver News'
    ws.append(['기사 제목'])

    for title in titles:
        ws.append([title])

    wb.save(filename)


def main() -> None:
    search_url = (
        'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8'
        '&query=%EB%B0%98%EB%8F%84%EC%B2%B4&ackey=9tiwdrio'
    )

    print('원본 검색 페이지를 요청합니다...')
    html = fetch_html(search_url)

    print('뉴스 탭 주소를 찾습니다...')
    news_tab_url = find_news_tab_url(html)
    if news_tab_url:
        print('뉴스 탭 페이지를 요청합니다:', news_tab_url)
        html = fetch_html(news_tab_url)
    else:
        print('뉴스 탭 주소를 찾지 못했습니다. 원본 페이지에서 기사 제목을 시도합니다.')

    titles = parse_news_titles(html)
    if not titles:
        print('기사 제목을 찾지 못했습니다. 페이지 구조가 변경되었을 수 있습니다.')
        return

    print(f'총 {len(titles)}개 기사 제목을 찾았습니다.')
    save_titles_to_excel(titles, 'naver_result.xlsx')
    print('naver_result.xlsx 파일로 저장했습니다.')


if __name__ == '__main__':
    main()
