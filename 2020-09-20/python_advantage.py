array = [ 5, 7, 9, 0, 3, 1, 6, 2, 4, 8 ]

def quick_sort(array):
    # 리스트 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = 