class ipl:
    
    def __init__(self,matchid,season,city,date,team1,team2,toss_winner,toss_decision,result,winner,
                      win_by_runs,win_by_wickets,playerofthematch,matches_won,venue):
        self.matchid=matchid
        self.season=season
        self.city=city
        self.date=date
        self.team1=team1
        self.team2=team2 
        self.toss_winner= toss_winner
        self.toss_decision=toss_decision
        self.result=result
        self.winner=winner
        self.win_by_runs=win_by_runs
        self.win_by_wickets=win_by_wickets
        self.playerofthematch=playerofthematch
        self.matches_won=matches_won
        self.venue=venue

class iplmatch:
    match=[]
    selectedmatch=[]

    def __init__(self,matchid,season,city,date,team1,team2,toss_winner,toss_decision,result,winner,
                      win_by_runs,win_by_wickets,playerofthematch,matches_won,venue):
        m=ipl(matchid,season,city,date,team1,team2,toss_winner,toss_decision,result,winner,
                         win_by_runs,win_by_wickets,playerofthematch,matches_won,venue)
        self.match.append(m)
    

    def show(self):
        print("===================AVAILABLE IPL MATCHES====================")
      
        pos=0
       
        for ipl in self.match:
         print("====================" ,pos," ===================")
         pos += 1
         self.display(ipl)

    def select(self):
        print("============SELECT THE MATCH============")
        print("============HOW MANY MATCHES YOU WANT?============")
        neededmatch=int(input())

        for i in range(0,neededmatch):
         print("=============INPUT THE MATCH NO===========")
         selectedmatch=int(input())
         print("============SELECTED MATCH===========")
         m=self.getiplById(selectedmatch - 1)
         self.selectedmatch.append(m)
         print(self.display(m))

    def getiplById(self,position):
         return self.match[position]


    def display(self,match):
         print("matchid :",match.matchid)
         print("season :",match.season)
         print("city :",match.city)
         print("date :",match.date)
         print("team1 :",match.team1)   
         print("team2 :",match.team2)
         print("toss_winner :",match.toss_winner) 
         print("toss_decision :",match.toss_decision) 
         print("result :",match.result) 
         print("winner :",match.winner)
         print("win_by_runs :",match.win_by_runs)
         print("win_by_wickets :",match.win_by_wickets)
         print("playerofthematch :",match.playerofthematch)
         print("matches_won:",match.matches_won)
         print("venue:",match.venue)

    def selectedmatch(self):
        return self.selectedmatch

class dataset:
   
    matches=[]
    def __init__(self,myBooks):
        self.match=myBooks
       
    def display(self):
        pos=0
        for match in self.match:
         print("==========DATASET ON MATCHES=========")
         pos +=1
         print("======== MATCH NO",pos,"=======")
         print("matchid:",match.matchid)
         print("season:",match.season)
         print("city:",match.city)
         print("date:",match.date)
         print("team1:",match.team1)   
         print("team2:",match.team2)
         print("toss_winner:",match.toss_winner) 
         print("toss_decision:",match.toss_decision) 
         print("result:",match.result) 
         print("winner:",match.winner)
         print("win_by_runs:",match.win_by_runs)
         print("win_by_wickets:",match.win_by_wickets)
         print("playerofthematch:",match.playerofthematch)
         print("matcheswon:",match.matcheswon)
         print("venue:",match.venue)


    def getTotal(self):
        total=sum(map(lambda m:m.matches_won,self.matches))
        print("========TOTAL WONS========")
        print(total)

    def delete(self):
        print("==========DO YOU WANT TO DELETE ANY MATCH NO ? 1=YES,0=NO")
        choice=int(input())
        if (choice ==1):
            print("============ENTER MATCH NO========")
            position=int(input())
            self.match.remove(self.getmatchById(position))
        else:
            print("===========NO MATCH NO DELETED========")

    def getmatchById(self,position):
        return self.match[position - 1]

    if "__MAIN__":

        print("=========WELCOME TO IPL MATCH DATA==========")

        im=iplmatch("1","2020","Bangalore","2020-04-19","RCB","KKR","RCB","fielding","normal","RCB",
                    "35","0","BB McCullum","2","chinnaswamy stadium")
        im=iplmatch("2","2020","chandigarh","2020-04-20","kings XI punjab","CSK","CSK","bating",
                       "normal","CSK","20","0","MEK Hussey","0","punjab stadium")
        im=iplmatch("3","2020","Mumbai","2020-04-22","MI","RCB","MI","bating","normal","RCB","10","0",
                        "MV Boucher","3","Wnakhede stadium")
        im=iplmatch("4","2020","Delhi" ,"2020-04-23","DD","RR","RR","fielding","normal","DD",
                      "0","9","Karley","1","Delhi stadium")

    im.show()
    im.select()

    selectedmatch=sm.selectedmatch()

    print(selectedmatch)
    d=dataset(selectedmatch)
    d.display()
    d.delete()
    d.getTotal()