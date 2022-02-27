#최대 힙 직접 구현
'''
<힙 정렬>
1. 힙을 만든다.(heapify함수)
2. root와 마지막 노드를 바꿔준다.
3. 이때 바꾼 노드는 없는 취급한다.
4. 새로운 root가 힙 속성을 지킬 수 있게 heapify호출
5. 모든 인덱스를 돌면서 반복한다.
'''

'''
<힙 정렬의 시간 복잡도>
1. 노드 개수 n개. n개 모두 heapify 함수를 거치면서 힙을 생성 -> O(nlog(n))
2. swap O(1)
3, 4. heapify 다시 호출 -> O(log(n))
5. n개 인덱스 돌면서 반복 -> O(nlog(n)))
=> O(nlog(n)) + O(nlog(n)) = O(nlog(n))
'''

def swap(tree, index_1, index_2):
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp

def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다


def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    parent_index = index // 2  # 삽입된 노드의 부모 노드의 인덱스 계산

    # 부모 노드가 존재하고, 부모 노드의 값이 삽입된 노드의 값보다 작을 때
    if 0 < parent_index < len(tree) and tree[index] > tree[parent_index]:
        swap(tree, index, parent_index)  # 부모 노드와 삽입된 노드의 위치 교환
        reverse_heapify(tree, parent_index)  # 삽입된 노드를 대상으로 다시 reverse_heapify 호출
        
        
class PriorityQueue:
    def __init__(self):
        self.heap = [None]  #리스트로 구현한 힙

    def insert(self, data):
        """삽입 메소드"""
        self.heap.append(data)  # 힙의 마지막에 데이터 추가
        reverse_heapify(self.heap, len(self.heap)-1) # 삽입된 노드(추가된 데이터)의 위치를 재배치

    def extract_max(self):
        """최우선순위 데이터 추출 메소드"""
        heap_len = len(self.heap)
        swap(self.heap, 1, heap_len-1)
        
        extracted_max = self.heap.pop()
        heapify(self.heap, 1, len(self.heap))
        
        return extracted_max

    def __str__(self):
        return str(self.heap)

# 출력 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)