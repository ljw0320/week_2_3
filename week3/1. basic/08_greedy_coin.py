"""
[그리디 알고리즘 - 거스름돈]

문제 설명:
- 그리디(Greedy) 알고리즘으로 거스름돈을 계산합니다.
- 가장 큰 단위의 동전부터 사용하여 최소 개수로 거슬러줍니다.
- 매 순간 최선의 선택(가장 큰 동전)을 합니다.

입력:
- change: 거슬러줄 금액
- coins: 사용 가능한 동전 종류 (예: [500, 100, 50, 10])

출력:
- 필요한 동전의 개수
- 각 동전의 사용 개수

예제:
입력: change = 1260, coins = [500, 100, 50, 10]
출력:
500원: 2개
100원: 2개
50원: 1개
10원: 1개
총 6개

힌트:
- 큰 동전부터 사용
- 현재 동전으로 최대한 거슬러주기
- 나머지 금액으로 다음 동전 사용
"""

"""
그리디 알고리즘으로 거스름돈 계산

Args:
    change: 거슬러줄 금액
    coins: 동전 종류 리스트 (큰 순서)

Returns:
    (총 개수, {동전: 개수} 딕셔너리)
"""

# 방법 1-1 : 반복문 사용(시간 복잡도 고려X)
def make_change_greedy(change, coins):
    result = {}
    total_coins = 0
    coin_count = []
    
    # TODO: 각 동전에 대해 반복
    ## 현재 동전으로 거슬러줄 수 있는 개수 계산    
    ## 개수가 0보다 크면 결과에 추가

    # 반복 로직: 현재 가격에서 가장 큰 동전의 가격을 빼줌
    # ex) 1260 - 500 = 760
    # 단, 빼주는 동전의 가격이 현재 가격보다 작거나 같아야 한다.
    # if max(coins) <= change :
    #   change = change - max(coins)
    # 다음으로 큰 동전으로 넘어가야 한다면? 반복문 사용!
    # 빼준 후에는 총 개수를 더해준다.
    # total = total+1
    # 사용한 동전을 딕셔너리에 담는다
    # result = {coin: 1}

    # 빼고 난 나머지가 다시 함수의 입력이 된다.
    # result = make_change_greedy(change, coins)

    # 나머지, 즉 change가 0이 될 때 까지 반복한다.
    # 주의할 점은 결과가 계속 쌓여야 한다는 것.
    # 입력된 동전 종류 리스트(coins)를 내림차순으로 미리 정렬(반복 횟수 줄이기 위함)
    # coins 내부 원소는 정렬은 바뀌더라도 원소 개수나 값이 바뀌면 안됨
    # 각 코인의 개수에 대한 변수    

    coins.sort(reverse=True)    

    while change !=0:
        for coin in coins:
            if coin > change:
                continue
            else :
                change = change - coin
                total_coins = total_coins + 1  
                # 빈 딕셔너리에 (키가 없는 경우) 방법                                          
                if coin not in result: 
                    result[coin] = 1
                else : 
                    result[coin] = result[coin]+1

                # # 더 간단하게 표현하면 아래와 같이 씀. 키가 없으면 0 반환함
                # result[coin] = result.get(coin, 0) + 1

                break
        
    return total_coins, result

# 방법 1-2 : 반복문 사용(반복 횟수 개선)
# pop을 사용하여 가격보다 큰 동전의 가격을 리스트에서 빼주면 반복 횟수가 줄어듬
# 오름차순으로 정렬하되, 반복문의 접근은 역순(내림차순)으로 함.(큰 수부터 접근)
def make_change_greedy_1(change, coins):
    total_coins = 0
    result = {}

    coins.sort()

    while change :
        for coin in coins[::-1]:
            if change >= coin:
                change = change - coin
                total_coins = total_coins + 1
                result[coin] = result.get(coin, 0) + 1 

                if change < coin: 
                    coins.pop()

                break

    return total_coins, result

# 방법 2 재귀 호출 사용
# 종료 조건 : change = 0
# 재귀 호출 줄어든 값(change-coin)
# 반환해야하는 값 : 
# - 사용한 코인 총 개수(정수 값)
# - 각 동전별 사용한 개수(딕셔너리)
# 재귀 호출을 어떻게 할 것인가?

def make_change_greedy_2(change, coins):
    total_coins = 0
    result = {}

    # 종료조건 : 넣은 금액이 0이 될 때 
    if change == 0 : 
        return total_coins, result

    # 동전 역순으로 정렬(최댓값부터 빼보기 위함)
    coins.sort(reverse=True)
    
    for coin in coins:
        if change >= coin:
            change = change - coin                        
            total_coins, result = make_change_greedy_2(change, coins)             
            total_coins += 1                                    
            result[coin] = result.get(coin, 0) + 1            
            break           

    return total_coins, result
        
# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    change1 = 1260
    coins1 = [500, 100, 50, 10]
    total, details = make_change_greedy_2(change1, coins1)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change1}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()
    
    # 테스트 케이스 2
    change2 = 4570
    coins2 = [500, 100, 50, 10]
    total, details = make_change_greedy_2(change2, coins2)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change2}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()
    
    # 테스트 케이스 3
    change3 = 1000
    coins3 = [500, 100, 50, 10]
    total, details = make_change_greedy_2(change3, coins3)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change3}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")


