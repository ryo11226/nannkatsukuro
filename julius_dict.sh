#!/bin/sh

#yomiファイルを作成
touch ~/lumos/julius/dict/bot.yomi
echo でんき でんき >> ~/lumos/julius/dict/bot.yomi
echo けして けして >> ~/lumos/julius/dict/bot.yomi
echo つけて つけて >> ~/lumos/julius/dict/bot.yomi
echo るうもす るうもす >> ~/lumos/julius/dict/bot.yomi
echo まきしま まきしま >> ~/lumos/julius/dict/bot.yomi
echo おふ おふ >> ~/lumos/julius/dict/bot.yomi
echo きょうの きょうの >> ~/lumos/julius/dict/bot.yomi
echo てんきは てんきは >> ~/lumos/julius/dict/bot.yomi

#phone
iconv -f utf8 -t eucjp ~/lumos/julius/dict/bot.yomi | ~/lumos/julius/julius-4.4.2.1/gramtools/yomi2voca/yomi2voca.pl | iconv -f eucjp -t utf8 > ~/lumos/julius/dict/bot.phone

#grammar
touch ~/lumos/julius/dict/bot.grammar
echo S : NS_B BOT NS_E >> ~/lumos/julius/dict/bot.grammar
echo BOT : DENKI KESHITE >> ~/lumos/julius/dict/bot.grammar
echo BOT : DENKI TSUKETE >> ~/lumos/julius/dict/bot.grammar
echo BOT : RUUMOSU >> ~/lumos/julius/dict/bot.grammar
echo BOT : RUUMOSU MAKISHIMA >> ~/lumos/julius/dict/bot.grammar
echo BOT : OFU >> ~/lumos/julius/dict/bot.grammar
echo BOT : KYOUNO TENNKIHA >> ~/lumos/julius/dict/bot.grammar

#voca
cat <<EOF > ~/lumos/julius/dict/bot.voca
% DENKI
でんき  d e N k i
% KESHITE
けして  k e sh i t e
% TSUKETE
つけて  ts u k e t e
% RUUMOSU
るうもす        r u u m o s u
% MAKISHIMA
まきしま        m a k i sh i m a
% OFU
おふ    o f u
% KYOUNO
きょうの        ky o u n o
% TENNKIHA
てんきは        t e N k i h a
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