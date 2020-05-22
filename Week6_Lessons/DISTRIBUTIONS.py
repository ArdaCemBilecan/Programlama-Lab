import random
import pylab

def rollDie():
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    result = ""
    for i in range(n):
        result = result+" "+str(rollDie())
    print(result)
    
    
def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.choice(['H','T']) == 'H':
            heads = heads+1
    return heads/numFlips



def flipSim(numFlipsPerTrial,numTrials):
    fracHeads=[]
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    return mean


def regressToMean(numFlips,numTrials):
    fracHeads=[]
    for i in range(numTrials):
        fracHeads.append(flip(numFlips))
    extremes,nextTrials=[],[]
    for i in range(len(fracHeads)-1):
        if fracHeads[i]<0.33 or fracHeads[i]>0.66:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i+1])
    
    pylab.plot(range(len(extremes)),extremes,'ko',label='Extreme')
    pylab.plot(range(len(nextTrials)),nextTrials,'k^',label = 'Next Trial')
    pylab.axhline(0.5)
    pylab.ylim(0,1)
    pylab.xlim(-1,len(extremes)+1)
    pylab.xlabel('Extreme Example and Next Trial')
    pylab.ylabel('Fractions Heads')
    pylab.title('Regression to Mean')
    pylab.legend(loc='best')
    
    
def flipPlot(minExp, maxExp): 
     ratios, diffs, xAxis = [], [], [] 
     for exp in range(minExp, maxExp + 1):  
         xAxis.append(2**exp)
     for numFlips in xAxis:
         numHeads = 0
         for n in range(numFlips):
             if random.choice(('H', 'T')) == 'H': 
                 numHeads += 1 
         numTails = numFlips - numHeads 
         try:
              ratios.append(numHeads/numTails)
              diffs.append(abs(numHeads - numTails))
         except ZeroDivisionError:
              continue
     pylab.title('Difference Between Heads and Tails')
     pylab.xlabel('Number of Flips')
     pylab.ylabel('Abs(#Heads - #Tails)') 
     pylab.plot(xAxis, diffs, 'k')
     pylab.figure()
     pylab.title('Heads/Tails Ratios')
     pylab.xlabel('Number of Flips')
     pylab.ylabel('#Heads/#Tails')
     pylab.plot(xAxis, ratios, 'k') 
 
    
def variance(X):
        mean = sum(X)/len(X)
        tot = 0.0
        for x in X:
            tot += (x - mean)**2
        return tot/len(X)
    
def stdDev(X):
    return variance(X)**0.5


def makePlot(xVals, yVals, title, xLabel, yLabel, style,logX = False, logY = False):
     pylab.figure()
     pylab.title(title)
     pylab.xlabel(xLabel)
     pylab.ylabel(yLabel)
     pylab.plot(xVals, yVals, style)
     if logX:
         pylab.semilogx()
     if logY:
         pylab.semilogy()
         
         
def runTrial(numFlips):
     numHeads = 0
     for n in range(numFlips):
         if random.choice(('H', 'T')) == 'H':
             numHeads += 1
     numTails = numFlips - numHeads
     return (numHeads, numTails) 



def flipPlot1(minExp, maxExp, numTrials):
     ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], [] 
     xAxis = []
     for exp in range(minExp, maxExp + 1):
         xAxis.append(2**exp)
     for numFlips in xAxis:
         ratios, diffs = [], []
         for t in range(numTrials):
             numHeads, numTails = runTrial(numFlips)
             ratios.append(numHeads/numTails)
             diffs.append(abs(numHeads - numTails))
         
         ratiosMeans.append(sum(ratios)/numTrials)
         diffsMeans.append(sum(diffs)/numTrials)
         ratiosSDs.append(stdDev(ratios))
         diffsSDs.append(stdDev(diffs))
     
     numTrialsString = ' (' + str(numTrials) + ' Trials)' 
     title = 'Mean Heads/Tails Ratios' + numTrialsString
     makePlot(xAxis, ratiosMeans, title, 'Number of flips','Mean Heads/Tails', 'ko', logX = True) 
     title = 'SD Heads/Tails Ratios' + numTrialsString 
     makePlot(xAxis, ratiosSDs, title, 'Number of Flips','Standard Deviation', 'ko', logX = True, logY = True) 
        
      
 

   
#
#random.seed(0) 
#flipPlot(4, 20)
    
flipPlot1(4,20,20)
            
            
            

