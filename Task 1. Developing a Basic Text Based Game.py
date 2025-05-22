{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a7c07e3-fbf7-4147-b625-3abcebf84d51",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "TASK 1: Develop a basic\n",
    "text-based game.\n",
    "\n",
    "Objective: Implement a simple game using\n",
    "conditional statements for game logic.\n",
    "\n",
    "Steps:\n",
    "\n",
    "1.Choose a game type (quiz, guessing game).\n",
    "2.Define the game rules and logic.\n",
    "3.Use conditional statements to manage\n",
    "game flow.\n",
    "4.Test and debug the game for correctness."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "848f9e79-93e4-439b-afbe-3689b9034e9c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "guess number 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "wrong guess\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "guess number 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "wrong guess\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "guess number 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "wrong guess\n",
      "you lost the game\n",
      "game is over\n"
     ]
    }
   ],
   "source": [
    "\n",
    "#step 1:playing guessing game\n",
    "\n",
    "#step 2:by using this random module it can pick one number from (1,9) #randomly\n",
    "   #we can use any number from 1 to 9999999\n",
    "   # when random number == guess number the ouput should be (\"you won the game\")\n",
    "   # when random number != guess number the ouput should be (\"you lost the game\")\n",
    "\n",
    "#step3 :\n",
    "import random\n",
    "fix=random.randint(1,9)#it will take one random number\n",
    "i=1\n",
    "while i<=3:\n",
    "    guess=int(input('guess number'))\n",
    "\n",
    "    if fix==guess:\n",
    "        print(\"you won the game\")\n",
    "    else:\n",
    "        print(\"wrong guess\")\n",
    "    i=i+1\n",
    "\n",
    "else:\n",
    "    print('you lost the game')\n",
    "print(\"game is over\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4004ce1-5916-4f18-b095-5281e1c2d1c2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
