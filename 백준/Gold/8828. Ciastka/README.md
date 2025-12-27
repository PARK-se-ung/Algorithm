# [Gold IV] Ciastka - 8828 

[문제 링크](https://www.acmicpc.net/problem/8828) 

### 성능 요약

메모리: 263780 KB, 시간: 2316 ms

### 분류

브루트포스 알고리즘, 정렬, 누적 합

### 제출 일자

2025년 12월 27일 21:28:19

### 문제 설명

<p>Hektor ze Zbyszkiem codziennie rano wybierają się po ciastka. Ciastkarz przygotowuje każdorazowo N ciastek, z których każde opisuje jedna liczba naturalna reprezentująca jego jakość. Chłopcy na zmianę wybierają po jednym ciastku, zawsze wybierając najlepsze z dostępnych jeszcze ciastek.</p>

<p>W tym tygodniu na Zbyszka przypada kolej dokonywania pierwszego wyboru, co jest zdaniem Hektora bardzo niesprawiedliwe. Hektor chciałby, żeby przewaga Zbyszka (suma jakości ciastek wybranych przez Zbyszka pomniejszona o sumę jakości ciastek Hektora) była możliwie mała. Aby osiągnąć ten cel postanowił uciec się do drobnej manipulacji. </p>

<p>Hektor zadzwonił wcześnie rano do kończącego pracę ciastkarza i zapytał o ciastka przygotowane na dzisiaj. Ciastkarz bardzo lubi Hektora i może na jego prośbę uzupełnić ten zbiór o jeszcze jedno jedno ciastko wybranej przez Hektora jakości.</p>

<p>Znając jakości przygotowanych ciastek i mogąc uzupełnić ten zbiór o maksymalnie jedno ciastko dowolnej ( naturalnej ) jakości oblicz minimalną osiągalną przewagę Zbyszka nad Hektorem.</p>

### 입력 

 <p>W pierwszej linii wejścia znajduje się liczba zestawów testowych Z ( 1 <= Z<= 10 ). Następniepodawane są kolejne zestawy testowe.</p>

<p>Każdy zestaw zaczyna się od liczby naturalnej N ( 1 <= N <= 1000000 ) oznaczającej liczbę ciastek przygotowanych przez ciastkarza.</p>

<p>W drugiej linii zestawu znajduje się N liczb naturalnych A<sub>i </sub>reprezentujących jakości kolejnych ciastek ( 1 <= A<sub>i</sub> <= 1000 ).</p>

### 출력 

 <p>Dla każdego przypadku testowego wypisz w osobnej linii minimalną różnicę pomiędzy jakością ciastek Zbyszka a jakością ciastek Hektora.</p>

