# Copyright 2020, Nathanael Bowley, All rights reserved.

"""todo:
    * add image to program
    * add more arabic words
    * add a search function to allow for searching for specific english / arabic words to add to study set
    * figure out if this could be ported to android to use on phone. 
    * improved ui?
    * change the incorrect statement to a percentage matching actual word statement
        Your response had 23% in common with the correct word. You answered INCORRECTLY!

wordPairs = {
    "as (adv.)":"metal",
    "as (conj.1)": "baynama",
    "as (conj.2)":"hasab",
    "as (prep.)": "ka",
    "as (pron.)": "athnaa'",
    "I":"",
    "his": "elu",
    "that":"",
    "he": "hewweh",
    "was":"",
    "for":"mshan",
    "on":"ala",
    "are":"",
    "with":"ma" }"""

# main loop.
while True:

    from random import randint
    import ast
    from dictionary import wordPairs
    from studySet import studySetPairs
    from dictionary import showWordPairs
    from studySet import showStudySetPairs

    print("English-Lebanese Study Tool")
    print("words version 0.1.1; Copyright 2020, Nathanael Bowley, All rights reserved.")
    print("Report issues on discord to Nay2D2#3241\n")

    while True:
        print("Would you like to review your personal study set?")
        studySet = input("Reply with yes or no: ")

        if studySet == "yes":
            if studySetPairs == {} or studySetPairs == "" or studySetPairs is None:
                print("\n---------------------------------------------------------------------------")
                print("   Study Set is currently empty! Use 'add ss' to add a word to study set")
                print("---------------------------------------------------------------------------\n")
                studySet = "no"
                wordPairs = wordPairs
                studySetBool = False
                break
            elif studySetPairs != {} or studySetPairs != "" or studySetPairs is not None:
                wordPairs = studySetPairs
                studySetBool = True
                break

        elif studySet == "no":
            wordPairs = wordPairs
            studySetBool = False
            break

    wordPairsLength = len(wordPairs)
    newEnglishList = list(wordPairs.keys())
    newLebaneseList = list(wordPairs.values())

    # user keywords
    remove = "remove"
    clearall = "clear all"
    commands = "commands"
    addToStudySet = "add ss"
    clearSS = "clear ss"
    back = "back"
    skip = "skip"
    nextWord = "next"
    allWordPairs = "show word pairs"
    allStudySetPairs = "show ss pairs"

    # checking to see if the user wants to have randomized language given or a specific one.
    print("Would you like to specify the language given?")
    chooseLanguage = ""
    while True:
        chooseLanguage = input("Choose one of the following: 'random', 'given english', 'given arabic': ")

        if chooseLanguage == 'random' or chooseLanguage == 'given english' or chooseLanguage == 'given arabic':
            break

    print("\n---------------------------------------------------------------")
    print("   Type 'commands' in the answer box for important features!")
    print("---------------------------------------------------------------")

    condition = True
    while condition:

        filename = 'file/Notepads/dontShow.txt'
        with open(filename, 'r') as inn:
            dontShowString = inn.read()

        if dontShowString == "":
            dontShow = {}
        else:
            dontShow = ast.literal_eval(f"{dontShowString}")

        randomWordIndex = randint(0, wordPairsLength - 1)

        randomEnglishOrLebanese = 0
        if chooseLanguage == 'random':
            randomEnglishOrLebanese = randint(0, 1)
        elif chooseLanguage == 'given english':
            randomEnglishOrLebanese = 0
        elif chooseLanguage == 'given arabic':
            randomEnglishOrLebanese = 1

        correctEnglish = newEnglishList[randomWordIndex]
        correctArabic = newLebaneseList[randomWordIndex]

        correctEnglishString = f'"{correctEnglish}"'
        correctArabicString = f'"{correctArabic}"'

        # consider making a percentage correct instead of just right or wrong?

        # input is 0 so we give an english word and request lebanese
        if randomEnglishOrLebanese == 0 and correctEnglish not in dontShow:

            print(f"\nWhat is {correctEnglishString} in Arabic?")
            userAnswer = input("Answer: ")

            if userAnswer == remove:

                # saying not to print it until clear all is applied
                print("This word will not be shown again until you answer with: clear all")

                # assigning the word pair to not show up anymore
                dontShow[correctEnglish] = correctArabic

                # writing the dictionary to file
                filename = 'file/Notepads/dontShow.txt'
                with open(filename, 'w') as out:
                    out.write(str(dontShow))

            elif userAnswer == clearall:
                print("you cleared the removed words, all words will now show")

                # writing empty to file
                filename = 'file/Notepads/dontShow.txt'
                with open(filename, 'w') as out:
                    out.write("")

            elif userAnswer == clearSS:
                print("you cleared the Study Set, all words will now show")

                # writing empty to file
                filename = 'file/Notepads/studySet.txt'
                with open(filename, 'w') as out:
                    out.write("")
                break

            elif userAnswer == commands:
                print("Command List:\n •remove - removes Arabic/English word pair from being asked",
                      "\n •clear all - WARNING: clears all removed words and allows the to reappear",
                      "\n •commands - recalls this list",
                      "\n •add ss - adds current word pair to your custom study set",
                      "\n •clear ss - WARNING: clears your entire custom study set",
                      "\n •back - returns you to the main menu of the program",
                      "\n •next - continues on to the next word pair",
                      f"\n •show word pairs - WARNING: all {len(showWordPairs)} word pairs will be shown",
                      f"\n •show ss pairs - WARNING: {len(showStudySetPairs)} word pairs in study set will be shown")

            elif userAnswer == addToStudySet:
                print(f"{correctEnglish} added to study set")
                studySetPairs[correctEnglish] = correctArabic

                # writing the dictionary to file
                filename = 'file/Notepads/studySet.txt'
                with open(filename, 'w') as out:
                    out.write(str(studySetPairs))

            elif userAnswer == back:
                print("\nRETURNING TO MAIN MENU...\n")
                break

            elif userAnswer == skip or userAnswer == nextWord:
                continue

            elif userAnswer == allWordPairs:
                print(f"WARNING: this will show all {len(showWordPairs)} word pairs are you sure?")
                while True:
                    userResponce = input("yes or no: ")
                    if userResponce == "yes":
                        for key, value in wordPairs.items():
                            key = "English: " + key
                            value = "Lebanese: " + value
                            print("%-30s" % key, end="")
                            print("%-30s" % value, sep=" ")
                        break
                    elif userResponce == "no":
                        break

            elif userAnswer == allStudySetPairs:
                print(f"WARNING: this will show all {len(showStudySetPairs)} word pairs are you sure?")
                while True:
                    userResponce = input("yes or no: ")
                    if userResponce == "yes":
                        for key, value in studySetPairs.items():
                            key = "English: " + key
                            value = "Lebanese: " + value
                            print("%-30s" % key, end="")
                            print("%-30s" % value, sep=" ")
                        break
                    elif userResponce == "no":
                        break

            elif userAnswer == correctArabic:
                print("CORRECT!")
            elif userAnswer != correctArabic:
                print("INCORRECT THE CORRECT ARABIC WORD IS:", correctArabicString)

        # input is 1 so we give a lebanese word and request english
        elif randomEnglishOrLebanese == 1 and correctEnglish not in dontShow:

            print(f"\nWhat is {correctArabicString} in Arabic?")
            userAnswer = input("Answer: ")

            if userAnswer == remove:

                # saying not to print it until clear all is applied
                print("This word will not be shown again until you answer with: clear all")

                # assigning the word pair to not show up anymore
                dontShow[correctEnglish] = correctArabic

                # writing the dictionary to file
                filename = 'file/Notepads/dontShow.txt'
                with open(filename, 'w') as out:
                    out.write(str(dontShow))

            elif userAnswer == clearall:
                print("you cleared the removed words, all words will now show")

                # writing empty to file
                filename = 'file/Notepads/dontShow.txt'
                with open(filename, 'w') as out:
                    out.write("")

            elif userAnswer == addToStudySet:
                print(f"{correctArabic} added to study set")
                studySetPairs[correctEnglish] = correctArabic

                # writing the dictionary to file
                filename = 'file/Notepads/studySet.txt'
                with open(filename, 'w') as out:
                    out.write(str(studySetPairs))

            elif userAnswer == clearSS:
                print("you cleared the Study Set, all words will now show")

                # writing empty to file
                filename = 'file/Notepads/studySet.txt'
                with open(filename, 'w') as out:
                    out.write("")
                break

            elif userAnswer == commands:
                print("Command List:\n •remove - removes Arabic/English word pair from being asked",
                      "\n •clear all - WARNING: clears all removed words and allows the to reappear",
                      "\n •commands - recalls this list",
                      "\n •add ss - adds current word pair to your custom study set",
                      "\n •clear ss - WARNING: clears your entire custom study set",
                      "\n •back - returns you to the main menu of the program",
                      "\n •next - continues on to the next word pair",
                      f"\n •show word pairs - WARNING: all {len(showWordPairs)} word pairs will be shown",
                      f"\n •show ss pairs - WARNING: {len(showStudySetPairs)} word pairs in study set will be shown")

            elif userAnswer == back:
                print("\nRETURNING TO MAIN MENU...\n")
                break

            elif userAnswer == skip or userAnswer == nextWord:
                continue

            elif userAnswer == allWordPairs:
                print(f"WARNING: this will show all {len(showWordPairs)} word pairs are you sure?")
                while True:
                    userResponce = input("yes or no: ")
                    if userResponce == "yes":
                        for key, value in wordPairs.items():
                            key = "English: " + key
                            value = "Lebanese: " + value
                            print("%-30s" % key, end="")
                            print("%-30s" % value, sep=" ")
                        break
                    elif userResponce == "no":
                        break

            elif userAnswer == allStudySetPairs:
                print(f"WARNING: this will show all {len(showStudySetPairs)} word pairs are you sure?")
                while True:
                    userResponce = input("yes or no: ")
                    if userResponce == "yes":
                        for key, value in studySetPairs.items():
                            key = "English: " + key
                            value = "Lebanese: " + value
                            print("%-30s" % key, end="")
                            print("%-30s" % value, sep=" ")
                        break
                    elif userResponce == "no":
                        break

            elif userAnswer == correctEnglish:
                print("CORRECT!")
            elif userAnswer != correctEnglish:
                print("INCORRECT THE CORRECT ENGLISH WORD IS:", correctEnglishString)
        elif len(dontShow) == len(wordPairs):
            print("it seems you cleared every single word, automatically clearing all")

            # writing empty to file
            filename = 'file/Notepads/dontShow.txt'
            with open(filename, 'w') as out:
                out.write("")

"""
they:
be:
at:
one:
have:
this:
from:"mn"
by:
hot:
word:
but:
what:
some:
is:
it:
you:
or:
had:
the:
of:
to:
and:
a:
in:
we:
can:
out:
other:
were:
which:
do:
their:
time:
if:
will:
how:
said:
an:
each:
tell:
does:
set:
three:
want:
air:
well:
also:
play:
small:
end:
put:
home:
read:
hand:
port:
large:
spell:
add:
even:
land:
here:
must:
big:
high:
such:
follow:
act:
why:
ask:
men:
change:
went:
light:
kind:
off:
need:
house:
picture:
try:
us:
again:
animal:
point:
mother:
world:
near:
build:
self:
earth:
father:
"""

"""
any
new
work
part
take
get
place
made
live
where
after
back
little
only
round
man
year
came
show
every
good
me
give
our
under
name
very
through
just
form
sentence
great
think
say
help
low
line
differ
turn
cause
much
mean
before
move
right
boy
old
too
same
she
all
there
when
up
use
your
way
about
many
then
them
write
would
like
so
these
her
long
make
thing
see
him
two
has
look
more
day
could
go
come
did
number
sound
no
most
people
my
over
know
water
than
call
first
who
may
down
side
been
now
find
head
stand
own
page
should
country
found
answer
school
grow
study
still
learn
plant
cover
food
sun
four
between
state
keep
eye
never
last
let
thought
city
tree
cross
farm
hard
start
might
story
saw
far
sea
draw
left
late
run
don’t
while
press
close
night
real
life
few
north
book
carry
took
science
eat
room
friend
began
idea
fish
mountain
stop
once
base
hear
horse
cut
sure
watch
color
face
wood
main
open
seem
together
next
white
children
begin
got
walk
example
ease
paper
group
always
music
those
both
mark
often
letter
until
mile
river
car
feet
care
second
enough
plain
girl
usual
young
ready
above
ever
red
list
though
feel
talk
bird
soon
body
dog
family
direct
pose
leave
song
measure
door
product
black
short
numeral
class
wind
question
happen
complete
ship
area
half
rock
order
fire
south
problem
piece
told
knew
pass
since
top
whole
king
street
inch
multiply
nothing
course
stay
wheel
full
force
blue
object
decide
surface
deep
moon
island
foot
system
busy
test
record
boat
common
gold
possible
plane
stead
dry
wonder
laugh
thousand
ago
ran
check
game
shape
equate
hot
miss
brought
heat
snow
tire
bring
yes
distant
fill
east
paint
language
among
unit
power
town
fine
certain
fly
fall
lead
cry
dark
machine
note
wait
plan
figure
star
box
noun
field
rest
correct
able
pound
done
beauty
drive
stood
contain
front
teach
week
final
gave
green
oh
quick
develop
ocean
warm
free
minute
strong
special
mind
behind
clear
tail
produce
fact
space
heard
best
hour
better
true
during
hundred
five
remember
step
early
hold
west
ground
interest
reach
fast
verb
sing
listen
six
table
travel
less
morning
ten
simple
several
vowel
toward
war
lay
against
pattern
slow
center
love
person
money
serve
appear
road
map
rain
rule
govern
pull
cold
notice
voice
energy
hunt
probable
bed
brother
egg
ride
cell
believe
perhaps
pick
sudden
count
square
reason
length
represent
art
subject
region
size
vary
settle
speak
weight
general
ice
matter
circle
pair
include
divide
syllable
felt
grand
ball
yet
wave
drop
heart
am
present
heavy
dance
engine
position
arm
wide
sail
material
fraction
forest
sit
race
window
store
summer
train
sleep
prove
lone
leg
exercise
wall
catch
mount
wish
sky
board
joy
winter
sat
written
wild
instrument
kept
glass
grass
cow
job
edge
sign
visit
past
soft
fun
bright
gas
weather
month
million
bear
finish
happy
hope
flower
clothe
strange
gone
trade
melody
trip
office
receive
row
mouth
exact
symbol
die
least
trouble
shout
except
wrote
seed
tone
join
suggest
clean
break
lady
yard
rise
bad
blow
oil
blood
touch
grew
cent
mix
team
wire
cost
lost
brown
wear
garden
equal
sent
choose
fell
fit
flow
fair
bank
collect
save
control
decimal
ear
else
quite
broke
case
middle
kill
son
lake
moment
scale
loud
spring
observe
child
straight
consonant
nation
dictionary
milk
speed
method
organ
pay
age
section
dress
cloud
surprise
quiet
stone
tiny
climb
cool
design
poor
lot
experiment
bottom
key
iron
single
stick
flat
twenty
skin
smile
crease
hole
jump
baby
eight
village
meet
root
buy
raise
solve
metal
whether
push
seven
paragraph
third
shall
held
hair
describe
cook
floor
either
result
burn
hill
safe
cat
century
consider
type
law
bit
coast
copy
phrase
silent
tall
sand
soil
roll
temperature
finger
industry
value
fight
lie
beat
excite
natural
view
sense
capital
won’t
chair
danger
fruit
rich
thick
soldier
process
operate
practice
separate
difficult
doctor
please
protect
noon
crop
modern
element
hit
student
corner
party
supply
whose
locate
ring
character
insect
caught
period
indicate
radio
spoke
atom
human
history
effect
electric
expect
bone
rail
imagine
provide
agree
thus
gentle
woman
captain
guess
necessary
sharp
wing
create
neighbor
wash
bat
rather
crowd
corn
compare
poem
string
bell
depend
meat
rub
tube
famous
dollar
stream
fear
sight
thin
triangle
planet
hurry
chief
colony
clock
mine
tie
enter
major
fresh
search
send
yellow
gun
allow
print
dead
spot
desert
suit
current
lift
rose
arrive
master
track
parent
shore
division
sheet
substance
favor
connect
post
spend
chord
fat
glad
original
share
station
dad
bread
charge
proper
bar
offer
segment
slave
duck
instant
market
degree
populate
chick
dear
enemy
reply
drink
occur
support
speech
nature
range
steam
motion
path
liquid
log
meant
quotient
teeth
shell
neck
oxygen
sugar
death
pretty
skill
women
season
solution
magnet
silver
thank
branch
match
suffix
especially
fig
afraid
huge
sister
steel
discuss
forward
similar
guide
experience
score
apple
bought
led
pitch
coat
mass
card
band
rope
slip
win
dream
evening
condition
feed
tool
total
basic
smell
valley
nor
double
seat
continue
block
chart
hat
sell
success
company
subtract
event
particular
deal
swim
term
opposite
wife
shoe
shoulder
spread
arrange
camp
invent
cotton
born
determine
quart
nine
truck
noise
level
chance
gather
shop
stretch
throw
shine
property
column
molecule
select
wrong
gray
repeat
require
broad
prepare
salt
nose
plural
anger
claim
continent
"""
