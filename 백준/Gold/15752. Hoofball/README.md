# [Gold IV] Hoofball - 15752 

[문제 링크](https://www.acmicpc.net/problem/15752) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

그래프 이론, 그래프 탐색, 정렬

### 제출 일자

2025년 12월 25일 21:49:26

### 문제 설명

<p>In preparation for the upcoming hoofball tournament, Farmer John is drilling his $N$ cows (conveniently numbered $1\dots N$, where $1 \leq N \leq 100$) in passing the ball. The cows are all standing along a very long line on one side of the barn, with cow $i$ standing $x_i$ units away from the barn ($1 \leq x_i \leq 1000$). Each cow is standing at a distinct location.</p>

<p>At the beginning of the drill, Farmer John will pass several balls to different cows. When cow $i$ receives a ball, either from Farmer John or from another cow, she will pass the ball to the cow nearest her (and if multiple cows are the same distance from her, she will pass the ball to the cow farthest to the left among these). So that all cows get at least a little bit of practice passing, Farmer John wants to make sure that every cow will hold a ball at least once. Help him figure out the minimum number of balls he needs to distribute initially to ensure this can happen, assuming he hands the balls to an appropriate initial set of cows.</p>

### 입력 

 <p>The first line of input contains $N$. The second line contains $N$ space-separated integers, where the $i$th integer is $x_i$.</p>

### 출력 

 <p>Please output the minimum number of balls Farmer John must initially pass to the cows, so that every cow can hold a ball at least once.</p>

