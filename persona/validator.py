def is_mbti_valid(value):
    valid_extensions = ['intj', 'intp', 'infj', 'infp',
                        'estj', 'estp', 'esfj', 'esfp',
                        'entj', 'entp', 'enfj', 'enfp',
                        'istj', 'istp', 'isfj', 'isfp']
    if not value.lower() in valid_extensions:
        return False
    else:
        return True


