'''
최대 100개의 자연수가 키로 입력
최대 heap
'''

def enq(n):
    global last
    last += 1
    tree[last] = n  # 완전 이진트리 유지
    c = last  # 새로 추가된 정점을 자식으로
    p = c // 2  # 완전 이진트리에서의 부모 정점 번호
    while p > 0 and tree[p] < tree[c]:  # 부모가 있고 자식의 키 값이 더 크면 교환
        tree[p], tree[c] = tree[c], tree[p]


# 포화 이진트리의 정점번호 1 ~ 100
tree = [0] * 101
last = 0  # 마지막 정점 번호