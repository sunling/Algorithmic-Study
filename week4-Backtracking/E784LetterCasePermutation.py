from typing import List

# GivenastringS, wecantransformeveryletterindividuallytobelowercase
# or uppercasetocreateanotherstring.
# Return a list of all possible strings we could create.
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not str:
            return []
        res = []

        for c in str:
            if c.isalpha():
                

    # def letterCasePermutation(self, S):
    #     L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
    #     return [''.join(i) for i in itertools.product(*L)]
