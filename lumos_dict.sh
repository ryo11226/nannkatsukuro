#!/bin/sh

#yomiファイルを作成
touch bot.yomi
echo でんき でんき >> bot.yomi
echo けして けして >> bot.yomi
echo つけて つけて >> bot.yomi

#phone
iconv -f utf8 -t eucjp ~/lumos/julius/dict/bot.yomi | ~/lumos/julius/julius-4.4.2.1/gramtools/yomi2voca/yomi2voca.pl | iconv -f eucjp -t utf8 > ~/lumos/julius/dict/bot.phone

touch bot.grammar
echo S : NS_B BOT NS_E >> bot.grammar
echo BOT : DENKI KESHITE >> bot.grammar
echo BOT : DENKI TSUKETE >> bot.grammar

#voca
cat <<EOF > bot.voca
% DENKI
でんき  d e N k i
% KESHITE
けして  k e sh i t e
% TSUKETE
つけて  ts u k e t e
% NS_B
[s] silB
% NS_E
[/s] silE
EOF

#dict
cd ~/lumos/julius/julius-4.4.2.1/gramtools/mkdfa
mkdfa.pl ~/lumos/julius/dict/bot

#test
julius -C ~/lumos/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip -gram ~/lumos/julius/dict/bot -input mic