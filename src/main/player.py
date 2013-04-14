#!/bin/env python

import pygame.midi
import soundvalue

class Player:

    def __init__(self):

        instrument = 22
        port = 2

        self.button2sound = {'a':(60,61), 's':(62,63), 'd':(64,65) }
        self.buttons = self.button2sound.keys()

        self.volume = 127
    
        pygame.midi.init()
        self.midiOutput = pygame.midi.Output(port, 0)
        self.midiOutput.set_instrument(instrument)

        self.currently_playing = {k : False for k in self.button2sound.iterkeys()}

    def play(self, key):
        note = self.button2sound[key][0]
        self.midiOutput.note_on(note,self.volume)
        self.currently_playing[key] = True

    def stop(self, key):
        note = self.button2sound[key][0]
        self.midiOutput.note_off(note,self.volume)
        self.currently_playing[key] = False

    def quit(self):
        pygame.midi.quit()
            

if __name__ == "__main__":
    p = Player()
    print(p.button2sound)

#import pygame
#import pygame.midi
#
#pygame.init()
#pygame.midi.init()
#
#pygame.display.set_mode((640,480))
#
#instrument = 22
#note = 74
#volume = 127
#port = 2
#
#midiOutput = pygame.midi.Output(port, 0)
#midiOutput.set_instrument(instrument)
#
#finished = False
#
#key2sound = {'a':60, 's':62, 'd':64 }
#
#print "Press q to quit..."
#currently_playing = {k : False for k in key2sound.iterkeys()}
#
#while not finished:
#
#  event =  pygame.event.wait()
#
#  if event.type == pygame.QUIT:
#    finished = True
#  elif event.type in (pygame.KEYDOWN,pygame.KEYUP):
#    key = pygame.key.name(event.key)
#    if key == 'q':
#      finished = True
#
#    if key in key2sound:
#      if event.type == pygame.KEYDOWN:
#        note = key2sound[key]
#        midiOutput.note_on(note,volume)
#        currently_playing[key] = True
#      elif event.type == pygame.KEYUP:
#        midiOutput.note_off(note,volume)
#        currently_playing[key] = False
#
#del midiOutput
#pygame.midi.quit()
#
#print "-- END --"
