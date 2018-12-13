import pyautogui as pg
import webbrowser as wb
import time as t

points = 0

show = pg.prompt ("what is your favorite show?")
if show == "Parks and Rec":
        points += 5
        wb.open ("https://www.youtube.com/watch?v=Tch4v0L0GHA")
        t.sleep(10)
        pg.alert ("that is a really good show!")
elif show == "the office":
        points += 5
        wb.open ("https://www.youtube.com/watch?v=M8KmqaJvgpE")
        t.sleep(10)
        pg.alert ("I love Dwight!")
elif show == "Daredevil":
        points += 5
        wb.open ("https://www.youtube.com/watch?v=t9AIXuXzp9E")
        t.sleep(10)
        pg.alert ("I can't believe it got canceled!")
elif show == "Arrow":
        points += 5
        wb.open ("https://www.youtube.com/watch?v=oftGEKCdAmY")
        t.sleep(10)
        pg.alert ("So intense!")
elif show == "Iron fist":
        points += 5
        pg.alert ("to fictional!")
elif show == "family guy":
        points -= 10
        pg.alert ("Legendary meme!")
else:
        points -= 10
        pg.alert("Your favorite show is" + show)

t.sleep(4)

favted = pg.prompt ("Who's your favorite Teddy?")

if favted == "Teddy Kim":
        points += 5
        wb.open("https://www.youtube.com/watch?v=wALUqN7YKI0")
        t.sleep(10)
        pg.alert ("He is lax bro and good at duo wipes!")
elif show == "Teddy Sandler!":
        points += 5
        wb.open("https://www.youtube.com/watch?v=iixbSmaXkjM")
        t.sleep(10)
        pg.alert ("he is sick at soccer")
elif show == "Teddy Minchin!":
        points -= 5
        wb.open("https://www.youtube.com/watch?v=R0MTO4aWkzg")
        t.sleep(10)
        pg.alert ("He is the V-bucks god!")
elif show == "Teddy Danforth!":
        points -= 15
        wb.open("https://www.google.com/search?q=teddy+danforth&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjOn4ab7LPeAhWSMd8KHcJaB1gQ_AUIDygC&biw=756&bih=684#imgrc=uFQyOYNsuNyw3M:")
        t.sleep(10)
        pg.alert ("What the Todd Rosenbaum")
elif show == "Teddy Harrington!":
        pg.alert ("he is the seventh grade history teacher.")
elif show == "Teddy Conners":
        pg.alert ("LMYL gang?")
else:
        points -= 10
        pg.alert ("your favorite Teddy is" + favted)

t.sleep(4)

sport = pg.prompt("what is your favorite sport? ")

if sport == "lacrosse":
        points += 5
        wb.open("https://www.youtube.com/watch?v=tmgqaBo3x3I")
        t.sleep(12)
        pg.alert ("Lax for life")
elif sport == "soccer":
        points += 5
        wb.open("https://www.youtube.com/watch?v=X0RyayUVGUE")
        t.sleep(10)
        pg.alert ("goolasoooooo")
elif sport == "football":
        wb.open("https://www.youtube.com/watch?v=U_DHpdrx0ZE")
        t.sleep(15)
        pg.alert ("what a hit son")
elif sport == "golf":
        wb.open("https://www.youtube.com/watch?v=70mYN75xd2k")
        t.sleep(10)
        pg.alert (" Jordan Spieth is the greatest golfer in the world")
elif sport == "hockey":
        wb.open("https://www.youtube.com/watch?v=v9EtLGwrJ58")
        t.sleep(12)
        pg.alert ("body good")
elif sport == "curling":
        points -= 5
        pg.alert ("not respectable")
else:
        points -= 5
        pg.alert ("ok nes")

t.sleep(4)

videogame = pg.prompt("what is your favorite video game? ")

if videogame == "fortnite":
        points += 5
        wb.open("https://www.youtube.com/watch?v=GPz79v5_i7E")
        t.sleep(10)
        pg.alert ("amen brother")
elif videogame == "fifa":
        points += 5
        wb.open("https://www.youtube.com/watch?v=orWEhzgrkns")
        t.sleep(10)
        pg.alert (" goolasoooooo")
elif videogame == "Madden":
        wb.open("https://www.youtube.com/watch?v=E8JLicvsVxU")
        t.sleep(10)
        pg.alert ("what a hit son")
elif videogame == "Rainbow Six Siege":
        wb.open("https://www.youtube.com/watch?v=9Delp8UXEzw")
        t.sleep(10)
        pg.alert ("It's taking over")
elif videogame == "NHL 19":
        pg.alert ("rip body good")
elif videogame == "Black Ops 4":
        points += 5
        pg.alert ("of course, it is respectable")
else:
        points -= 5
        pg.alert ("ok nes")

t.sleep(4)

fish = pg.prompt("what is your favorite fish? ")

if fish == "Striped Bass":
        points += 5
        wb.open("https://www.youtube.com/watch?v=HFnLkDXZodA")
        t.sleep(15)
        pg.alert (" where have they been this year")
elif fish == "Porgy":
        points += 5
        wb.open("https://www.youtube.com/watch?v=wbEq-0JH7m4")
        t.sleep(13)
        pg.alert (" Their population growth is frightening")
elif fish == "Bluefish":
        points += 5
        wb.open("https://www.youtube.com/watch?v=Nd5d7WeGKGc")
        t.sleep(14)
        pg.alert ("They will spool your line")
elif fish == "flounder":
        wb.open("https://www.youtube.com/watch?v=sb3afDcPS8E")
        t.sleep(10)
        pg.alert (" They are in between seasons.")
elif fish == "false albacore":
        pg.alert ("They come into the sound for such a short period of time.")
elif fish == "Bluefin tuna":
        pg.alert ("Hopefully they don't go extinct!")
else:
        points -= 10
        pg.alert ("ok I see")

pg.alert("You scored: " + str(points))

