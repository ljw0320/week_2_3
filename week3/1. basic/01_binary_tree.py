"""
[이진 트리 - Binary Tree 기본]

문제 설명:
- 이진 트리의 기본 구조를 구현합니다.
- 각 노드는 최대 2개의 자식(왼쪽, 오른쪽)을 가집니다.
- 전위, 중위, 후위 순회를 구현합니다.
- 각 노드가 최대 2개의 자식 노드(왼쪽, 오른쪽)를 가질 수 있는 트리 구조.

입력:
- 트리 노드들

출력:
- 전위 순회: 루트 → 왼쪽 → 오른쪽
- 중위 순회: 왼쪽 → 루트 → 오른쪽
- 후위 순회: 왼쪽 → 오른쪽 → 루트

예제:
트리 구조:
      1
     / \
    2   3
   / \
  4   5

전위: [1, 2, 4, 5, 3]
중위: [4, 2, 5, 1, 3]
후위: [4, 5, 2, 3, 1]

힌트:
- 재귀로 간단히 구현 가능
- 순회 순서만 다름
"""

"""
재귀 함수 조건
1) base case : 종료 조건
2) 재귀 호출

# arr.append(value) vs arr +=value의 차이
  append() : 값을 하나의 원소로 추가
    arr = [1, 2, 3]
    arr.append([4, 5])

    print(arr) => [1, 2, 3, [4, 5]]

  += : 오른쪽의 iterable을 '풀어서' 이어 붙임(각각의 '순회 가능한' 값을 추가)  (extend()와 거의 유사)
    arr = [1, 2, 3]
    arr += [4, 5]

    print(arr) => [1, 2, 3, 4, 5]  
    
    # 중요한 차이점
    arr = [1, 2, 3]
    arr.append(4)   # 가능
    arr += 4        # 오류
    4는 순회 가능한 값이 아니므로 4를 추가하고 싶다면 리스트로 감싸야 한다.
    arr += [4]

    # 문자열의 경우도 차이가 있다. 
        arr = [1, 2]
        arr += "abc" => [1, 2, 'a', 'b', 'c']

        arr = [1, 2]
        arr.append("abc") => [1, 2, 'abc']
        
"""

"""
arr1 = [1, 2, 3]
arr1.append([4,5])

arr2 = [1, 2, 3]
arr2+=[4,5]

arr3 = [1, 2, 3]
arr3.extend([4,5])

print(arr1, arr2, arr3)
"""

# 재귀함수 시각화 #
# from function_visualizer import FunctionVisualizer    
# visualizer = FunctionVisualizer()

# @visualizer.visualize(param_names=["n"])
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

# result = fib(10)

# visualizer.render("preorder")
# 재귀함수 시각화 #

class TreeNode:
    """이진 트리 노드"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# def preorder(root):
#     """전위 순회: 루트 → 왼쪽 → 오른쪽"""
#     result = []
    
#     # TODO: root가 None이면 빈 리스트 반환
#     if root is None:
#         return []
    
#     # TODO: 루트 값 추가    
#     result.append(root.value)
        
#     # TODO: 왼쪽 서브트리 순회        
#     result += preorder(root.left)
    
#     # TODO: 오른쪽 서브트리 순회    
#     result += preorder(root.right)    
    
#     return result

# append의 경우 인자 자체를 원소로 받기 때문에 
# 리스트도 원소로 입력되어 출력이 의도와 달라진다.
# def preorder(root):
#     """전위 순회: 루트 → 왼쪽 → 오른쪽"""
#     result = []
    
#     # TODO: root가 None이면 빈 리스트 반환
#     if root is None:
#         return []
    
#     # TODO: 루트 값 추가    
#     result.append(root.value)
        
#     # TODO: 왼쪽 서브트리 순회        
#     result.append(preorder(root.left))
    
#     # TODO: 오른쪽 서브트리 순회    
#     result.append(preorder(root.right))
    
#     return result

# extend의 경우 입력된 배열을 풀어서 각각을 원소로 저장한다.
# 따라서 +=과 같은 결과가 출력된다.
def preorder(root):
    """전위 순회: 루트 → 왼쪽 → 오른쪽"""
    result = []
    
    # TODO: root가 None이면 빈 리스트 반환
    if root is None:
        return []
    
    # TODO: 루트 값 추가    
    result.append(root.value)
        
    # TODO: 왼쪽 서브트리 순회        
    result.extend(preorder(root.left))
    
    # TODO: 오른쪽 서브트리 순회    
    result.extend(preorder(root.right))
    
    return result

def inorder(root):
    """중위 순회: 왼쪽 → 루트 → 오른쪽"""
    result = []
    
    # TODO: root가 None이면 빈 리스트 반환
    if root is None:
        return []    
    
    # TODO: 왼쪽 서브트리 순회
    result += inorder(root.left)
    
    # TODO: 루트 값 추가
    result.append(root.value)
    
    # TODO: 오른쪽 서브트리 순회
    result += inorder(root.right)
    
    return result

def postorder(root):
    """후위 순회: 왼쪽 → 오른쪽 → 루트"""
    result = []
    
    # TODO: root가 None이면 빈 리스트 반환
    if root is None:
        return []
    
    # TODO: 왼쪽 서브트리 순회
    result += postorder(root.left)
    
    # TODO: 오른쪽 서브트리 순회
    result += postorder(root.right)
    
    # TODO: 루트 값 추가
    result.append(root.value)
        
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 트리 생성:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("=== 이진 트리 순회 ===")
    print(f"전위 순회: {preorder(root)}")
    print(f"중위 순회: {inorder(root)}")
    print(f"후위 순회: {postorder(root)}")

