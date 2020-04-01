import sys

#Autores:
#Victor Vasconcellos Borba 31716369
#Pedro Giuliano Farina     31734391

#Para executar o código abra o shell no linux
#Insira o seguinte comando: cat input.txt | python3 so.py

def arrayGenerator(qtd):
  array=[]

  for i in range(qtd):

    array.append(0)

  return array


def ExecuteFifo(TimeInRow):

  WaitingTimexFifo=0

  EscFifo=0

  for time in TimeInRow:

    WaitingTimexFifo+=time

    WaitingTimexFifo+=1

    EscFifo+=1

  EscFifo-=1

  WaitingTimexFifo-=1

  return (EscFifo, WaitingTimexFifo)


def ExecuteSJF(TimeInRow):

  WaitingTimexSJF=0

  EscSJF=0

  for time in TimeInRow:

    WaitingTimexSJF+=time

    WaitingTimexSJF+=1

    EscSJF+=1

  EscSJF-=1

  WaitingTimexSJF-=1

  return (EscSJF, WaitingTimexSJF)


def calculaWaiting(TimeInRow, WaitingTime):

  WaitingTimesp=0

  ValorAntigo=0

  for i in range(0, len(TimeInRow)-1):

    WaitingTimesp=ValorAntigo+TimeInRow[i]+WaitingTimesp

    ValorAntigo+=TimeInRow[i]

  for x in range(1, len(TimeInRow)):

    WaitingTimesp-=WaitingTime[i]

  WaitingTimesp+=i

  WaitingTimesp=WaitingTimesp/(i+2)

  return WaitingTimesp

def orderTempo(TimeInRow2):

  n=len(TimeInRow2)

  for i in range(n):

    for j in range(0, n-i-1):

      if TimeInRow2[j]> TimeInRow2[j+1] :

        TimeInRow2[j], TimeInRow2[j+1]=TimeInRow2[j+1], TimeInRow2[j]

  return TimeInRow2


def ExecuteRR(TimeInRowRR, WaitingTime):

  scale=0

  RRWaitingTime=0

  RREsp=arrayGenerator(len(TimeInRowRR))

  RRESPFinal=arrayGenerator(len(TimeInRowRR))

  time=0

  n=len(TimeInRowRR)

  while(n!=0):

    for i in range (len(TimeInRowRR)):

      if(n==0):

        break

      if(TimeInRowRR[i]!=0):

        for j in range(2):

          if(TimeInRowRR[i]!=0):

            TimeInRowRR[i]=TimeInRowRR[i]-1

            for t in range(len(TimeInRowRR)):

              if i!=t:

                if WaitingTime[t] <= time:

                  RREsp[t] = ArithmeticError

            time += 1

            if(TimeInRowRR[i] == 0):

              n -= 1

              RRESPFinal[i]=RREsp[i]

        scale += 1

        time += 1

  for i in range(len(RRESPFinal)):

    RRWaitingTime=RRWaitingTime

  RRWaitingTime= RRWaitingTime+scale

  RRWaitingTime=RRWaitingTime/len(RRESPFinal)

  return (time, RRWaitingTime, scale)


def orderPRIO(WaitingTimePRIORITY, TimeInRowPRIORITY, PRIORITY2):

  n=len(TimeInRow)

  for i in range(n):

    for j in range(0, n-i-1):

      if PRIORITY2[j]>PRIORITY2[j+1] :

        PRIORITY2[j], PRIORITY2[j+1]=PRIORITY2[j+1], PRIORITY2[j]

        WaitingTimePRIORITY[j], WaitingTimePRIORITY[j+1]=WaitingTimePRIORITY[j+1], WaitingTimePRIORITY[j]

        TimeInRowPRIORITY[j], TimeInRowPRIORITY[j+1]=TimeInRowPRIORITY[j+1], TimeInRowPRIORITY[j]

  return (WaitingTimePRIORITY, TimeInRowPRIORITY, PRIORITY2)


def ExecutePRIO(WaitingTime, TimeInRow, PRIORITY):

  PrioWaitingTime=0

  PRIORITYEsp=arrayGenerator(len(TimeInRow))

  PRIORITYESPFinal=arrayGenerator(len(TimeInRow))

  PRIORITY2=PRIORITY.copy()

  TimeInRowPRIORITY=TimeInRow.copy()

  WaitingTimePRIORITY=WaitingTime.copy()

  (WaitingTimePRIORITY, TimeInRowPRIORITY, PRIORITY2)=orderPRIO(WaitingTimePRIORITY, TimeInRowPRIORITY, PRIORITY2)

  n=len(PRIORITY)

  Time=0

  Esc=0

  lastProcess=0

  while(n != 0):

    for i in range(len(PRIORITY2)):

      if  TimeInRowPRIORITY[i] != 0:

        if WaitingTimePRIORITY[i] <= Time:

          TimeInRowPRIORITY[i] -= 1

          for t in range(len(TimeInRow)):

              if i!=t:

                if WaitingTime[t]<=Time:

                  PRIORITYEsp[t]+=1

          if lastProcess != i:

            Esc += 1

            lastProcess=i

          Time += 1

        if TimeInRowPRIORITY[i] == 0:

          PRIORITYESPFinal[i]=PRIORITYEsp[i]

          n -= 1

        break

  Time=Time + Esc

  for i in range(len(PRIORITYESPFinal)):

    PrioWaitingTime=PRIORITYESPFinal[i]+ PrioWaitingTime

  PrioWaitingTime= PrioWaitingTime+Esc

  PrioWaitingTime=PrioWaitingTime/len(PRIORITYESPFinal)

  return (PrioWaitingTime, Esc, Time)


def FIFO(WaitingTime, TimeInRow):

  WaitingTimex=0

  Esc=0

  (EscFifo, WaitingTimexFifo)=ExecuteFifo(TimeInRow)

  WaitingFifo=calculaWaiting(TimeInRow, WaitingTime)

  print ("FIFO", "{:.2f}".format(WaitingTimexFifo), "{:.2f}".format(EscFifo), "{:.2f}".format(WaitingFifo))


def SJF(WaitingTime, TimeInRow):

  TimeInRow2=TimeInRow.copy()

  TimeInRow2=orderTempo(TimeInRow2)

  (EscSJF, WaitingTimexSJF)=ExecuteSJF(TimeInRow2)

  WaitingSJF=calculaWaiting(TimeInRow2, WaitingTime)

  print("SJF", "{:.2f}".format(WaitingTimexSJF), "{:.2f}".format(EscSJF), "{:.2f}".format(WaitingSJF))

def RR(WaitingTime, TimeInRow):

  TimeInRowRR=TimeInRow.copy()

  (time, RRWaitingTime, scale)=ExecuteRR(TimeInRowRR, WaitingTime)

  print("RR", "{:.2f}".format(time), "{:.2f}".format(scale), "{:.2f}".format(RRWaitingTime))


def PRIO(WaitingTime, TimeInRow, PRIORITY):

  (PrioWaitingTime, Esc, Time)=ExecutePRIO(WaitingTime, TimeInRow, PRIORITY)

  print("PRIO",  "{:.2f}".format(Time), "{:.2f}".format(Esc), "{:.2f}".format(PrioWaitingTime))

processos=[]

TimeInRow=[]

WaitingTime=[]

PRIORITY=[]

for line in sys.stdin:

  line=line.split(" ")

  line=[item.strip() for item in line]

  processos.append(line)

for line in processos:

  WaitingTime.append(line[0])

  TimeInRow.append(line[1])

  PRIORITY.append(line[2])

for i in range(len(WaitingTime)):

  WaitingTime[i]=int(WaitingTime[i])

  TimeInRow[i]=int(TimeInRow[i])

  PRIORITY[i]=int(PRIORITY[i])

#EXECUÇÃO

FIFO(WaitingTime, TimeInRow)

SJF(WaitingTime, TimeInRow)

RR(WaitingTime, TimeInRow)

PRIO(WaitingTime, TimeInRow, PRIORITY)
