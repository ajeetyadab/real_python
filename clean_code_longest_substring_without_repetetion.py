import string 
import fitz


def pdf_to_text(path):
    text = ""
    with fitz.open(path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Example usage

text = pdf_to_text("C:/Users/hp/Desktop/great_life.pdf")

# text = """ I stared at the crowd and told the biggest lie of my life.
# “James Waters was the best man I ever knew.” I didn’t know the guy. An hour ago, I didn’t even know his name. If his goofy face hadn’t been framed next to his casket, I wouldn’t even know what he looked like. I didn’t know he even existed. Well, he didn’t anymore, so that was a moot point.
# It was still uncertain if this was my biggest lie—it depended on whether or not it would fall apart. But it was certainly about to get bigger because people in the room were still waiting for me to go on.
# “When I first met him at Better Days a year ago, I thought he was an asshole.”
# Someone in the back gasped; overlapping murmurs spread through the small chapel. I could see several people in the front pews giving me dirty looks. A woman dabbing her eyes with a crumpled tissue was glaring at me, as if waiting for God’s wrath to strike me where I stood.
# You and me both, lady. I was wondering, too, if I was about to burst into flames.
# “While we all shared our stories, he just sat there, unaffected, like a block of wood.”
# James Waters had never attended Better Days, a support group for depression, because it didn’t exist.
# Or maybe it did. The name had a nice ring to it, after all.
# “He’d show up early just to open the windows—said he didn’t want to suffocate from our emotions. Sometimes he'd get so grumpy that people would walk out mid-session.”
# People were visibly shifting in their seats—unease grew in the room like it was a palpable thing. A few were throwing furtive glances around, as if daring others to put an end to my insults to James’s memories.
# Unperturbed, I pressed on, “But one day, when Jenna—one of the other attendees—was sharing her story, James suddenly got up from his chair, hugged her, and started crying like a baby. That’s when I knew the man had a heart. And from then on, he became the force behind the group.”
# People leaned forward, some clutching their chests, hanging onto my every word now.
# “He started giving us little notes, with our own words from the last session—to remind us of things that made us sound more brave than we felt. One day, he brought kids’ coloring books ‘for our inner child’. It was so cheesy that we decided to paint his face instead. And, shockingly, he let us. None of us had laughed that much in a long time."
# Boy, was I chucking it. But lying was its own language, and once you’ve had enough practice, it becomes as easy as any other.
# “When I relapsed and stopped coming around, he made an entire playlist of ‘whale music’, which I’d told him calmed me—and showed up at my house. I lost it when I saw him at the door. He just walked in without a word, put the music on, and we spent the whole day listening to whale sounds in silence."
# The woman, who now had wet tissue flakes clinging to her face like confetti, loudly blew her nose into the overused wad. Tears were pouring from her eyes in droves. Around her, others had begun to sob as well.
# For a fraction of a fraction of a moment I felt guilt rise up, but I sucked it back in, and it was once again lost in my chest like inhaled breath. I find whale sounds calming, as if I could understand them—at least that much wasn’t a lie.
# “He used to say, ‘We’ll never die, if we only keep flying.’”
# Who knows if James might have said that to someone, but he definitely didn’t say it to me or this nonexistent group. 
# I even wondered: Has anyone ever said that to anyone?
# But by then, a version of him had already taken shape in my mind—and the James I knew was exactly the kind of man who would have said those words.
# “I remember rolling my eyes at his declaration. I mean, who wouldn’t?”
# Subtle, unwitting laughter rang out in the room. I’ve realised that people would laugh at anything; all it took was turning on the right setting.
# “When I asked him if he thought we were some kind of vampires who would live forever? He simply gave me one of his looks—which neither confirmed nor denied it.”
# Words had started pouring out of me without much thought; it was as if my version of James himself was telling me what to say next.
# “Maybe he believed he was a vampire, and that’s why he flew off the roof?”
# Suddenly, the room was doused in tense silence. It was a crass thing to say about someone who had, in fact, flown off the roof. Apparently, that’s how he died. They had to hold a closed casket viewing for the poor fucker. But I had a point, which I needed to make fast—before someone chucked a shoe at me, or god himself showed up with lightning in hand.
# “Even though he tried to fly and we failed to catch him—he didn’t fail us. He gave us hope at Better Days, when he clearly had none. He held us together, even when he was falling apart. And I can say with certainty that his presence alone saved lives—it sure as hell saved mine”.
# With my head bowed, my voice thick with just the right emotion, I tell the crowd, “James Waters might be out of sight, but he will never be out of memory and mind. And even though he wasn't a vampire, he’ll live on in our hearts forever.”
# I lifted my eyes to see that people were openly bawling now. Some leaning into each other, some with their faces buried in their hands. Even those pretending they weren’t, were discreetly swiping at their eyes.
# I could feel my own throat closing up, tears stinging at the corners of my eyes.
# *** As a seasoned funeral crasher, I shouldn’t have made the mistakes I did today.
# Usually, I just observed and tried to piece together what happened by being on the periphery. But things got a little out of hand when I ran into Grandma Rose. I was already intrigued by how a thirty-something man might have died so young, and she seemed easy to ply with questions.
# Or, so I thought.
# Normally, I’d ask questions and answer questions with even more questions. That way, I walked away with fragments of the puzzle, leaving people with little more than what I'd found them with.
# But Grandma Rose—with joints crackling like frail sticks—turned out to be a booby trap I didn’t see coming.
# Perhaps it was her eyes, which grew as large as hen's eggs with my every word, that sucked me in. Or maybe it was the sobering realization that she believed her grandson had tried to live before giving up.
# Either way, she got me talking to the point where I was struggling to keep up with James Waters's make-believe secret life.
# At one point, she leaned closer, eyes keen in her wrinkled face, and asked, “Why do you think he…did it?”
# A bead of sweat ran down my back, as long moments of silence filled the space between us.
# I finally broke the silence by admitting, “I wish I knew. But I don’t.” Because some questions shouldn’t be answered with lies, even if they remain unanswered forever.
# Everything that followed was a blur—her wet face pressing into my chest, her tearfully thrusting me onto the podium, urging me to share the never-before-known details of James’s struggles. The lies that rolled out so easily, paved with years of practice. The hugging and crying that kept coming, as if people were trying to absorb James’s memories through my skin.
# After my little speech, I was dreading the questions.
# Surely, someone would ask: Which days did the group meet? Where were the other members? Why didn’t Better Days show up in a Google search? Why wasn't my name (fake name) in James’s phone book?
# I kept waiting for the question that would unravel the whole thing.
# But it never came.
# It was as if they also wanted to believe in my version of James.
# ***
# By the time I extracted myself from the throng of James’s family and friends, I was ready to sleep for days. Lying to a room full of people about a dead man turned out to be more exhausting than I imagined.
# I don’t remember what drew me to a stranger’s funeral the first time, but once I started, I couldn’t stop, and more than that—I didn’t want to.
# Most days, I can’t even decide what fascinates me about it.
# Maybe it’s that I don’t need to give away any part of me, to be a part of something. Or for a few hours, I can be someone—anyone else—other than me. Perhaps it’s the hopelessness that clings to the air, a longing for something unattainable. Or the challenge: will today be the day I tell a lie so big that it falls apart? And the anticipation of that.
# But I suspect it’s the moment when I peer into the casket—and there it is—death’s peace. Not an abstraction, but real enough that I can touch it with my fingertips. It's a relief, like no other, to see that life didn’t matter—because this is where it always ended, the only truth in the middle of all the lies.
# Before walking away, I looked one last time at James’s photo, surrounded by white roses, in dismay—because the James I knew would have preferred the red ones.
# And then I gave him a two-finger salute—for being the best man I never knew."""

# print(text)


# table = str.maketrans("","",string.punctuation)


# text = text.translate(table)
# print(text)

# text_list = text.split()
# print(text_list)


# longest_word = []
# length = 0
# for word in text_list:

#     clean = word.lower()
#     if not clean:
#         continue

#     if len(set(word)) == len(word):
#         if len(word)>  length:
#             longest_word = [word]
#             length = len(word)

#         elif len(word) == length:
#             longest_word.append(word)

    


# print(longest_word,length)
    


def clean_word(word):
    return word.translate(str.maketrans("","",string.punctuation))


def has_unique_charecter(word):

    return len(set(word)) == len(word)

def longest_unique_word(strings):

    longest_substring_length = 0
    longest_substring = []

    splitted_string = strings.split()

    for word in splitted_string:
        clean_worded = clean_word(word)
        clean_worded = clean_worded.lower()


        if not clean_worded:
            continue


        if has_unique_charecter(clean_worded):
            if len(clean_worded)>longest_substring_length:
                longest_substring = [clean_worded]
                longest_substring_length = len(clean_worded)

            elif len(clean_worded) == longest_substring_length:
                longest_substring.append(clean_worded)

    return longest_substring,longest_substring_length
            

text = """At Z-Library, we are thrilled to see a recent study highlighting the positive impact our platform has on students overcoming academic poverty. The research found that access to our vast collection of free e-books and articles has significantly helped students improve their academic performance and excel in their studies. We are proud to be able to provide a valuable resource that levels the playing field for students from all backgrounds. The study serves as a testament to the importance of open access to information and the role it plays in breaking down barriers to education. We are committed to continuing to provide free and easy access to knowledge for all. 
"""

print(longest_unique_word(text))