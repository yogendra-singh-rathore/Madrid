
def stringspliting(func):
    def innerfunction(strobject,splStep,sep=None,final=None):
        index=0
        result = ""
        final = []
        for i in strobject:
            result +=i
            if len(result) == splStep:
                final.append(result)
                result=""
        return final
    return innerfunction()

@stringspliting
def testFun(Strobject=None,splStep=None,sep=None,final=None):
    return final

print(testFun(strobject="Yogendra",splStep=3))