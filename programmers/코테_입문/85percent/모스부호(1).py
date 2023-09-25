def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }

    temp = [i for i in letter.split()]

    for i in temp:
        for k,v in morse.items():
            if i == k:
                answer += v

    return answer
    # return ''.join([morse[i] for i in letter.split(' ')])


print(solution(".... . .-.. .-.. ---"))
print(solution(".--. -.-- - .... --- -."))

