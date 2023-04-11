from scipy import stats

chat_id = 843200348


def solution(x, y) -> bool:
    alpha = 0.03

    p_val = stats.ttest_ind(x, y).pvalue
    return p_val < alpha
