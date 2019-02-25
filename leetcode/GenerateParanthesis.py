"""* Generate Parentheses
* Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
* For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
* """
class GenerateParanthesis(object):
    def generate(self, num):
        self.res = []
        if num<0: return self.res
        self.generatep(num, num, "", self.res)
        return self.res

    def generatep(self, leftp, righp, prog, res):
        if leftp == 0 and righp == 0:
            self.res.append(prog)
            return
        if leftp > 0:
            self.generatep(leftp-1, righp, prog+"(", self.res)
        if leftp < righp:
            self.generatep(leftp, righp-1, prog+")", self.res)

gp = GenerateParanthesis()
print(gp.generate(3))
print(len(gp.generate(10)))
print(gp.generate(0))
