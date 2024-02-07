#!/bin/bash

#COLORS
RED="\033[0;31m"
GREEN="\033[0;32m"
BLUE="\033[0;34m"
PURPEL="\033[0;35m"
YELLOW="\033[1;33m"
RESET="\033[0m"

# welcome displays a welcome message
welcome(){
    printf "$PURPEL
             ██████╗ ██████╗██╗      █████╗ ███████╗███████╗
            ██╔════╝██╔════╝██║     ██╔══██╗██╔════╝██╔════╝
            ██║     ██║     ██║     ███████║███████╗███████╗
            ██║     ██║     ██║     ██╔══██║╚════██║╚════██║
            ╚██████╗╚██████╗███████╗██║  ██║███████║███████║
             ╚═════╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝$RESET
                    Made by:$RED 0xj4gu4r$RESET\n"
    
}

# taking libraries from the user and add them nto the header file
take_libraries(){
    printf "$BLUE""Libraries:$RESET do you want to add an other library beside <ostream> & <string> for the$PURPEL $1$RESET class:\n"
    printf "[1]$GREEN yes\n$RESET[2]$RED no$RESET\n>>: "
    while read ch; do
        if [[ "$ch" != "1" && "$ch" != "2" ]]; then
            printf "\r$RED""Wrong choice:$RESET $ch try again\n>>: "
        elif [ $ch == "2" ]; then
            break
        else
            printf "\r$BLUE""Entre library: $RESET"
            while read LIB; do
                if [ -z $LIB ]; then
                    printf "\r$GREEN""Libraries added succefully.$RESET\n"
                    break
                fi
                echo "#include<$LIB>" >> $1
                printf "\r$BLUE""Entre library$RED[leave empty to exit]: $RESET"
            done
            break
        fi
    done
    echo >> $1
}

# taking private atributes and add them to the headr and there getter and setter to the .cpp file
take_prv_atr(){
    printf "\r$BLUE""Private Attributes:$RESET Do you want to add some private attributes for the$PURPEL $1$RESET class:\n"
    printf "[1]$GREEN yes\n$RESET[2]$RED no$RESET\n>>: "
    while read ch; do
        if [[ "$ch" != "1" && "$ch" != "2" ]]; then
            printf "\r$RED""Wrong choice:$RESET $ch try again\n>>: "
        elif [ $ch == "2" ]; then
            break
        else
            echo "  private:" >> "$1.hpp"
            printf "\r$BLUE""Entre the Private Attribute as follows$RED[leave empty to exit]: $RESET<$YELLOW""Type$RESET> <$YELLOW""Vrbl_Name$RESET>\n>>: "
            while read tp nm; do
                if [[ -z "$tp" || -z "$nm" ]]; then
                    printf "\r$GREEN""Private attributes added succefully.$RESET"
                    break
                fi
                echo "      $tp $nm;" >> "$1.hpp"
                echo "// $nm GETTER" >> "$1.cpp"
                echo "$tp $1::get$nm(void) const {return this->$nm;}" >> "$1.cpp"
                echo >> "$1.cpp"
                echo "// $nm SETTER" >> "$1.cpp"
                echo "void $1::set$nm($tp $nm) {this->$nm = $nm;}" >> "$1.cpp"
                echo >> "$1.cpp"
                echo "$tp get$nm(void) const;" >> /tmp/"$1.tmp"
                echo "void set$nm($tp $nm);" >> /tmp/"$1.tmp"
                printf "\r$BLUE""Entre the Private Attribute as follows$RED[leave empty to exit]: $RESET<$YELLOW""Type$RESET> <$YELLOW""Vrbl_Name$RESET>\n>>: "
            done
            break
        fi
    done

}

# setting up the public section of the class
take_pbl_atr(){
    echo "  public:" >> "$1.hpp"
    printf "$BLUE""Canonical Form:$RESET Do you want the$PURPEL $1$RESET class to be on the Canonical Form:\n"
    printf "[1]$GREEN yes\n$RESET[2]$RED no$RESET\n>>: "
    while read ch; do
        if [[ "$ch" != "1" && "$ch" != "2" ]]; then
            printf "\r$RED""Wrong choice:$RESET $ch try again\n>>: "
        elif [ $ch == "2" ]; then
            break
        else
            echo "      $1(void);" >> "$1.hpp"
            echo "      $1($1 const &obj);" >> "$1.hpp"
            echo "      $1 &operator=($1 const &obj);" >> "$1.hpp"
            echo "      ~$1(void);" >> "$1.hpp"
            break
        fi
    done
    echo
    if [[ -e "/tmp/$1.tmp" ]]; then
        echo "      // getters and setters" >> "$1.hpp"
        while read line; do
            echo "      $line" >> "$1.hpp"
        done < /tmp/"$1.tmp"
    fi
    printf "\r$BLUE""Public Attributes:$RESET Do you want to add some public attributes for the$PURPEL $1$RESET class:\n"
    printf "[1]$GREEN yes\n$RESET[2]$RED no$RESET\n>>: "
    while read ch; do
        if [[ "$ch" != "1" && "$ch" != "2" ]]; then
            printf "\r$RED""Wrong choice:$RESET $ch try again\n>>: "
        elif [ $ch == "2" ]; then
            break
        else
            printf "\r$BLUE""Entre the Public attributes: $RESET"
            while read atr; do
                if [ -z "$atr" ];then
                    break
                fi
                echo "      $atr;" >> "$1.hpp"
                printf "\r$BLUE""Entre the Public attributes$RED[leave empty to exit]: $RESET"
            done
            break
        fi
    done
    rm /tmp/"$1.tmp"
    printf "\r$GREEN""Public attributes added succefully.$RESET\n"
}

# Create the .cpp and .hpp files and make them ready to use
create_files(){
    HDR="$1.hpp"
    COD="$1.cpp"
    echo "#pragma once" > $HDR
    echo "#include"'"'"$HDR"'"' > $COD
    echo >> $HDR
    echo >> $COD
    echo "#include<string>" >> $HDR
    echo "#include<iostream>" >> $HDR
    # taking additional libraries
    take_libraries $HDR
    # using std namespace
    printf "\r$BLUE""Name Space:$RESET Do you want to use the standared name space for the$PURPEL $1$RESET class:\n"
    printf "[1]$GREEN yes\n$RESET[2]$RED no$RESET\n>>: "
    while read ch; do
        if [[ "$ch" != "1" && "$ch" != "2" ]]; then
            printf "\r$RED""Wrong choice:$RESET $ch try again\n>>: "
        elif [ $ch == "2" ]; then
            break
        else
            echo "using namespace std;" >> $HDR
            echo >> $HDR
            printf "\r$GREEN""NameSpace added succefully.$RESET\n"
            break
        fi
    done
    echo "class $1 {" >> $HDR
    # taking private attributes 
    take_prv_atr $1
    # taking public attributes
    take_pbl_atr $1
    echo "};" >> $HDR
}

#dispalying the welcome msg
welcome

if [ $# -eq 1 ] && [ $1 == "update" ]; then
    cd ~/.tools/cclass
    git pull
    exit
fi

#checking if there is argiments
if [ $# -lt 1 ]; then
    printf "$RED""ERROR:$RESET"" Not enough arguments\n$YELLOW""Usage:$RESET cclass [class name] ...\n"
    exit 1
fi

#creating classes's files
for CLS in "$@"
do
    create_files $CLS
    printf "\r$GREEN""$CLS created succefully.$RESET\n"
done

