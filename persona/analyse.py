def get_mbti(traits):
    i = traits.get('introverted', 0)
    e = traits.get('extraverted', 0)
    n = traits.get('intuitive', 0)
    s = traits.get('sensing', 0)
    t = traits.get('thinking', 0)
    f = traits.get('feeling', 0)
    j = traits.get('judging', 0)
    p = traits.get('perceiving', 0)
    mbti = ''
    if i > e:
        mbti += 'I'
    # elif i < e:
    #     mbti += 'E'
    else:
        mbti += 'E'
    if n > s:
        mbti += 'N'
    # elif n < s:
    #     mbti += 'S'
    else:
        mbti += 'S'

    if t > f:
        mbti += 'T'
    # elif t < f:
    #     mbti += 'F'
    else:
        mbti += 'F'

    if j > p:
        mbti += 'J'
    # elif j < p:
    #     mbti += 'P'
    else:
        mbti += 'P'
    return mbti
