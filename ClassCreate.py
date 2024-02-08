import sys, os, subprocess, time
# from sys import argv
from colorama import Fore, Style, init

init()

from typing import TextIO

#taking Libraries form the user
def takeLibraries(Hdr: TextIO, Cls: str):
    print(f"\r{Fore.BLUE}Libraries : {Style.RESET_ALL}Do you want to add an other library beside <ostream> & <string> for the {Fore.CYAN}{Cls}{Style.RESET_ALL} class:")
    ch = input(f"\t\t{Fore.GREEN}[1] ✓ {Style.RESET_ALL}| {Fore.RED}[2] ✘{Style.RESET_ALL}\n")
    while ch.isdecimal() == False or (int(ch) != 1 and int(ch) != 2):
            print(f"\r{Fore.RED}Wrong choice: {Style.RESET_ALL} try again: ", flush=True, end='')
            ch = input()
    if int(ch) == 1:
        print(f"Inter Libraries sperated by [{Fore.BLUE},{Style.RESET_ALL}]: ", end='', flush=True)
        lib = input().split(',')
        for x in lib:
            print(f"#include<{x}>" , end='\n', file=Hdr)
        print(f"{Fore.GREEN}SUCCESSES : {Style.RESET_ALL} The Libraries added Successfully to the Headr {Fore.CYAN}{Cls+'.hpp'}{Style.RESET_ALL}\n")
    
#Creating the Class
def creatClass(Hdr: TextIO, Cod: TextIO, Cls: str):
    print("class", Cls, '{', file=Hdr)
    print("\tprivate:", file=Hdr)
    print(f"{Fore.BLUE}Private Attributes : {Style.RESET_ALL}Do you want to add private attributes for the {Fore.CYAN}{Cls}{Style.RESET_ALL} class:")
    ch = input(f"\t\t{Fore.GREEN}[1] ✓ {Style.RESET_ALL}| {Fore.RED}[2] ✘{Style.RESET_ALL}\n")
    while ch.isdecimal() == False or (int(ch) != 1 and int(ch) != 2):
        print(f"\r{Fore.RED}Wrong choice: {Style.RESET_ALL} try again: ", flush=True, end='')
        ch = input()
    if int(ch) == 1:
        print(f"Inter Private attributes separated by [{Fore.BLUE}<type> <name> {Fore.WHITE}|{Fore.BLUE} ... {Style.RESET_ALL}]: ", end='', flush=True)
        atr = input().split(' | ')
        for x in atr:
            var = x.split(' ')
            if var[1][0].isalpha() and var[1][0].islower():var[1] = var[1][0].upper() + var[1][:-1]
            print(f"\t\t{var[0]} {var[1]};", file=Hdr)
        print("\tpublic:", file=Hdr)
        for x in atr:
            var = x.split(' ')
            if var[1][0].isalpha() and var[1][0].islower():var[1] = var[1][0].upper() + var[1][:-1]
            print(f"\t\t{var[0]} get{var[1]}(void) const;", file=Hdr)
            print(f"{var[0]} {Cls}::get{var[1]}(void) const ", '{return this->', var[1], ';}\n', sep='', file=Cod)
    else:
        print("\tpublic:", file=Hdr)
    print(f"{Fore.BLUE}Public Attributes : {Style.RESET_ALL}Do you want to add public attributes for the {Fore.CYAN}{Cls}{Style.RESET_ALL} class:")
    ch = input(f"\t\t{Fore.GREEN}[1] ✓ {Style.RESET_ALL}| {Fore.RED}[2] ✘{Style.RESET_ALL}\n")
    while ch.isdecimal() == False or (int(ch) != 1 and int(ch) != 2):
        print(f"\r{Fore.RED}Wrong choice: {Style.RESET_ALL} try again: ", flush=True, end='')
        ch = input()
    if int(ch) == 1:
        print(f"Inter Public attributes separated by [{Fore.BLUE}<type> <name> {Fore.WHITE}|{Fore.BLUE} ... {Style.RESET_ALL}]: ", end='', flush=True)
        atr = input().split(' | ')
        for x in atr:
            var = x.split(' ')
            print(f"\t\t{var[0]} {var[1]};", file=Hdr)
    print("};", file=Hdr)


def create_files(Cls):
    with open(Cls+'.cpp', 'w') as Cod, open(Cls+'.hpp', 'w') as Hdr:
        Hdr.write('''#pragma once

#include<iostream>
#include<string>
''')
        Cod.write(f"#include\"{Cls+'.hpp'}\"\n")
        takeLibraries(Hdr, Cls)
        print(f"{Fore.BLUE}Name Space : {Style.RESET_ALL}Do you want to use the standared name space for the {Fore.CYAN}{Cls}{Style.RESET_ALL} class:")
        ch = input(f"\t\t{Fore.GREEN}[1] ✓ {Style.RESET_ALL}| {Fore.RED}[2] ✘{Style.RESET_ALL}\n")
        while ch.isdecimal() == False or (int(ch) != 1 and int(ch) != 2):
            print(f"\r{Fore.RED}Wrong choice: {Style.RESET_ALL} try again: ", flush=True, end='')
            ch = input()
        if int(ch) == 1:
            print("\nusing namespace std;", end='\n', file=Hdr)
            print(f"{Fore.GREEN}SUCCESSES : {Style.RESET_ALL} The standerd name space added Successfully to the Headr {Fore.CYAN}{Cls+'.hpp'}{Style.RESET_ALL}\n")
        creatClass(Hdr, Cod, Cls)
        