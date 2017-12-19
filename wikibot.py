import praw
import time
import re
import requests
import bs4

path = "commented.txt"

def authenticate():
  print("Authenticating...\n")
  #reddit = praw.Reddit('wikibot',user_agent = 'web:wiki-bot:v0.1 (by /u/The_Senpat)')
  reddit = praw.Reddit(client_id='R16vtWU89Twrag',
                     client_secret="HRfn5yqjpiISU2zRTQkKDj8RFTw", password='spbot3password',
                     user_agent='spb3 by /u/TheSenpat', username='spb3')
  print('Authenticated as {}\n'.format(reddit.user.me()))
  return reddit

def run_wikibot(reddit):
    print('getting 250 comments...\n')
    
    for comment in reddit.subreddit('test').comments(limit = 250):
        if "!WikiBot" in comment.body:
            print('Link found with comment ID: ' + comment.id)
            
            #check to see if comment id is in the file
            file_obj_r = open(path,'r')
    
            if comment.id not in file_obj_r.read().splitlines():
                
                splitted = comment.body.split(" ")
                if(splitted.index("!WikiBot") + 2 > splitted.length-1):
                  string1 = splitted[splitted.index("!WikiBot")+1]
                  string2 = splitted[splitted.index("!WikiBot")+2]
                
                  print('Link is unique...posting explanation for ' + string1 + ' ' + string2 + '\n')
                  comment.reply('(' + string1 + ' ' + string2 + ')[wikipedia.com/wiki/'+string1+'_'+string2']')                 
                  file_obj_r.close()

                  file_obj_w = open(path,'a+')
                  file_obj_w.write(comment.id + '\n')
                  file_obj_w.close()
                else:
                  print('not complete')
            else:
                print('Already visited link...no reply needed\n')
            
            #comment.reply('hi')
            
            time.sleep(60)
            
            
def main():
    print("main2")
    reddit = authenticate()
    print("main3")
    while True:
        run_wikibot(reddit)
      
if __name__ == '__main__':
    print("main1")
    main()
