def solution(weights):
    # 중복 제거 및 오름차순 정렬
    unique_weights = sorted(set(weights))

    dp = [0] * (sum(unique_weights) + 1)
    dp[0] = 1  # base case

    # 각 weight에 대해
    for weight in unique_weights:
        for i in range(sum(unique_weights), -1, -1):
            if dp[i]:
                # weight를 추가하거나 두 배한 weight를 추가
                dp[i + weight] = max(dp[i + weight], dp[i] + 1)
                dp[i + 2 * weight] = max(dp[i + 2 * weight], dp[i] + 2)

    return max(dp)


print(solution([2, 2, 2, 2, 3, 3, 5, 6]))