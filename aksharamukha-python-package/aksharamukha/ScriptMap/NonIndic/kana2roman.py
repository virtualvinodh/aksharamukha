#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
try:
    from functools import cmp_to_key
except ImportError:
    # for python < 3.2; nicked from python 3.2
    def cmp_to_key(mycmp):
        """Convert a cmp= function into a key= function"""
        class K(object):
            __slots__ = ['obj']
            def __init__(self, obj):
                self.obj = obj
            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0
            def __gt__(self, other):
                return mycmp(self.obj, other.obj) > 0
            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0
            def __le__(self, other):
                return mycmp(self.obj, other.obj) <= 0
            def __ge__(self, other):
                return mycmp(self.obj, other.obj) >= 0
            def __ne__(self, other):
                return mycmp(self.obj, other.obj) != 0
            __hash__ = None
        return K



#
# Ruby/Romkan - a Romaji <-> Kana conversion library for Ruby.
#
# Copyright (C) 2001 Satoru Takabayashi <satoru@namazu.org>
#     All rights reserved.
#     This is free software with ABSOLUTELY NO WARRANTY.
#
# You can redistribute it and/or modify it under the terms of
# the Ruby's licence.
#

# This table is imported from KAKASI <http://kakasi.namazu.org/> and modified.

KUNREITAB = """ァ       xa      ア       a       ィ       xi      イ       i       ゥ       xu
ウ       u       ヴ       vu      ヴァ      va      ヴィ      vi      ヴェ      ve
ヴォ      vo      ェ       xe      エ       e       ォ       xo      オ       o

カ       ka      ガ       ga      キ       ki      キャ      kya     キュ      kyu
キョ      kyo     ギ       gi      ギャ      gya     ギュ      gyu     ギョ      gyo
ク       ku      グ       gu      ケ       ke      ゲ       ge      コ       ko
ゴ       go

サ       sa      ザ       za      シ       si      シャ      sya     シュ      syu
ショ      syo     シェ    sye
ジ       zi      ジャ      zya     ジュ      zyu     ジョ      zyo
ス       su      ズ       zu      セ       se      ゼ       ze      ソ       so
ゾ       zo

タ       ta      ダ       da      チ       ti      チャ      tya     チュ      tyu
チョ      tyo     ヂ       di      ヂャ      dya     ヂュ      dyu     ヂョ      dyo
ティ    ti

ッ       xtu
ッヴ      vvu     ッヴァ     vva     ッヴィ     vvi
ッヴェ     vve     ッヴォ     vvo
ッカ      kka     ッガ      gga     ッキ      kki     ッキャ     kkya
ッキュ     kkyu    ッキョ     kkyo    ッギ      ggi     ッギャ     ggya
ッギュ     ggyu    ッギョ     ggyo    ック      kku     ッグ      ggu
ッケ      kke     ッゲ      gge     ッコ      kko     ッゴ      ggo     ッサ      ssa
ッザ      zza     ッシ      ssi     ッシャ     ssya
ッシュ     ssyu    ッショ     ssyo    ッシェ     ssye
ッジ      zzi     ッジャ     zzya    ッジュ     zzyu    ッジョ     zzyo
ッス      ssu     ッズ      zzu     ッセ      sse     ッゼ      zze     ッソ      sso
ッゾ      zzo     ッタ      tta     ッダ      dda     ッチ      tti     ッティ  tti
ッチャ     ttya    ッチュ     ttyu    ッチョ     ttyo    ッヂ      ddi
ッヂャ     ddya    ッヂュ     ddyu    ッヂョ     ddyo    ッツ      ttu
ッヅ      ddu     ッテ      tte     ッデ      dde     ット      tto     ッド      ddo
ッドゥ  ddu
ッハ      hha     ッバ      bba     ッパ      ppa     ッヒ      hhi
ッヒャ     hhya    ッヒュ     hhyu    ッヒョ     hhyo    ッビ      bbi
ッビャ     bbya    ッビュ     bbyu    ッビョ     bbyo    ッピ      ppi
ッピャ     ppya    ッピュ     ppyu    ッピョ     ppyo    ッフ      hhu     ッフュ  ffu
ッファ     ffa     ッフィ     ffi     ッフェ     ffe     ッフォ     ffo
ッブ      bbu     ップ      ppu     ッヘ      hhe     ッベ      bbe     ッペ    ppe
ッホ      hho     ッボ      bbo     ッポ      ppo     ッヤ      yya     ッユ      yyu
ッヨ      yyo     ッラ      rra     ッリ      rri     ッリャ     rrya
ッリュ     rryu    ッリョ     rryo    ッル      rru     ッレ      rre
ッロ      rro

ツ       tu      ヅ       du      テ       te      デ       de      ト       to
ド       do      ドゥ    du

ナ       na      ニ       ni      ニャ      nya     ニュ      nyu     ニョ      nyo
ヌ       nu      ネ       ne      ノ       no

ハ       ha      バ       ba      パ       pa      ヒ       hi      ヒャ      hya
ヒュ      hyu     ヒョ      hyo     ビ       bi      ビャ      bya     ビュ      byu
ビョ      byo     ピ       pi      ピャ      pya     ピュ      pyu     ピョ      pyo
フ       hu      ファ      fa      フィ      fi      フェ      fe      フォ      fo
フュ    fu
ブ       bu      プ       pu      ヘ       he      ベ       be      ペ       pe
ホ       ho      ボ       bo      ポ       po

マ       ma      ミ       mi      ミャ      mya     ミュ      myu     ミョ      myo
ム       mu      メ       me      モ       mo

ャ       xya     ヤ       ya      ュ       xyu     ユ       yu      ョ       xyo
ヨ       yo

ラ       ra      リ       ri      リャ      rya     リュ      ryu     リョ      ryo
ル       ru      レ       re      ロ       ro

ヮ       xwa     ワ       wa      ウィ    wi      ヰ wi      ヱ       we      ウェ      we
ヲ       wo      ウォ    wo      ン n

ン     n'
ディ   dyi
ー     -
チェ    tye
ッチェ     ttye
ジェ      zye
"""

KUNREITAB_H = """ぁ      xa      あ      a      ぃ      xi      い      i      ぅ      xu
う      u      う゛      vu      う゛ぁ      va      う゛ぃ      vi       う゛ぇ      ve
う゛ぉ      vo      ぇ      xe      え      e      ぉ      xo      お      o

か      ka      が      ga      き      ki      きゃ      kya      きゅ      kyu
きょ      kyo      ぎ      gi      ぎゃ      gya      ぎゅ      gyu      ぎょ      gyo
く      ku      ぐ      gu      け      ke      げ      ge      こ      ko
ご      go

さ      sa      ざ      za      し      si      しゃ      sya      しゅ      syu
しょ      syo      じ      zi      じゃ      zya      じゅ      zyu      じょ      zyo
す      su      ず      zu      せ      se      ぜ      ze      そ      so
ぞ      zo

た      ta      だ      da      ち      ti      ちゃ      tya      ちゅ      tyu
ちょ      tyo      ぢ      di      ぢゃ      dya      ぢゅ      dyu      ぢょ      dyo

っ      xtu
っう゛      vvu      っう゛ぁ      vva      っう゛ぃ      vvi
っう゛ぇ      vve      っう゛ぉ      vvo
っか      kka      っが      gga      っき      kki      っきゃ      kkya
っきゅ      kkyu      っきょ      kkyo      っぎ      ggi      っぎゃ      ggya
っぎゅ      ggyu      っぎょ      ggyo      っく      kku      っぐ      ggu
っけ      kke      っげ      gge      っこ      kko      っご      ggo      っさ      ssa
っざ      zza      っし      ssi      っしゃ      ssya
っしゅ      ssyu      っしょ      ssyo
っじ      zzi      っじゃ      zzya      っじゅ      zzyu      っじょ      zzyo
っす      ssu      っず      zzu      っせ      sse      っぜ      zze      っそ      sso
っぞ      zzo      った      tta      っだ      dda      っち      tti
っちゃ      ttya      っちゅ      ttyu      っちょ      ttyo      っぢ      ddi
っぢゃ      ddya      っぢゅ      ddyu      っぢょ      ddyo      っつ      ttu
っづ      ddu      って      tte      っで      dde      っと      tto      っど      ddo
っは      hha      っば      bba      っぱ      ppa      っひ      hhi
っひゃ      hhya      っひゅ      hhyu      っひょ      hhyo      っび      bbi
っびゃ      bbya      っびゅ      bbyu      っびょ      bbyo      っぴ      ppi
っぴゃ      ppya      っぴゅ      ppyu      っぴょ      ppyo      っふ      hhu
っふぁ      ffa      っふぃ      ffi      っふぇ      ffe      っふぉ      ffo
っぶ      bbu      っぷ      ppu      っへ      hhe      っべ      bbe      っぺ    ppe
っほ      hho      っぼ      bbo      っぽ      ppo      っや      yya      っゆ      yyu
っよ      yyo      っら      rra      っり      rri      っりゃ      rrya
っりゅ      rryu      っりょ      rryo      っる      rru      っれ      rre
っろ      rro

つ      tu      づ      du      て      te      で      de      と      to
ど      do

な      na      に      ni      にゃ      nya      にゅ      nyu      にょ      nyo
ぬ      nu      ね      ne      の      no

は      ha      ば      ba      ぱ      pa      ひ      hi      ひゃ      hya
ひゅ      hyu      ひょ      hyo      び      bi      びゃ      bya      びゅ      byu
びょ      byo      ぴ      pi      ぴゃ      pya      ぴゅ      pyu      ぴょ      pyo
ふ      hu      ふぁ      fa      ふぃ      fi      ふぇ      fe      ふぉ      fo
ぶ      bu      ぷ      pu      へ      he      べ      be      ぺ      pe
ほ      ho      ぼ      bo      ぽ      po

ま      ma      み      mi      みゃ      mya      みゅ      myu      みょ      myo
む      mu      め      me      も      mo

ゃ      xya      や      ya      ゅ      xyu      ゆ      yu      ょ      xyo
よ      yo

ら      ra      り      ri      りゃ      rya      りゅ      ryu      りょ      ryo
る      ru      れ      re      ろ      ro

ゎ      xwa      わ      wa      ゐ      wi      ゑ      we
を      wo      ん      n

ん     n'
でぃ   dyi
ー     -
ちぇ    tye
っちぇ      ttye
じぇ      zye
"""

HEPBURNTAB = """ァ      xa      ア       a       ィ       xi      イ       i       ゥ       xu
ウ       u       ヴ       vu      ヴァ      va      ヴィ      vi      ヴェ      ve
ヴォ      vo      ェ       xe      エ       e       ォ       xo      オ       o


カ       ka      ガ       ga      キ       ki      キャ      kya     キュ      kyu
キョ      kyo     ギ       gi      ギャ      gya     ギュ      gyu     ギョ      gyo
ク       ku      グ       gu      ケ       ke      ゲ       ge      コ       ko
ゴ       go

サ       sa      ザ       za      シ       shi     シャ      sha     シュ      shu
ショ      sho     シェ    she
ジ       ji      ジャ      ja      ジュ      ju      ジョ      jo
ス       su      ズ       zu      セ       se      ゼ       ze      ソ       so
ゾ       zo

タ       ta      ダ       da      チ       chi     チャ      cha     チュ      chu
チョ      cho     ヂ       di      ヂャ      dya     ヂュ      dyu     ヂョ      dyo
ティ    ti

ッ       xtsu
ッヴ      vvu     ッヴァ     vva     ッヴィ     vvi
ッヴェ     vve     ッヴォ     vvo
ッカ      kka     ッガ      gga     ッキ      kki     ッキャ     kkya
ッキュ     kkyu    ッキョ     kkyo    ッギ      ggi     ッギャ     ggya
ッギュ     ggyu    ッギョ     ggyo    ック      kku     ッグ      ggu
ッケ      kke     ッゲ      gge     ッコ      kko     ッゴ      ggo     ッサ      ssa
ッザ      zza     ッシ      sshi    ッシャ     ssha
ッシュ     sshu    ッショ     ssho    ッシェ  sshe
ッジ      jji     ッジャ     jja     ッジュ     jju     ッジョ     jjo
ッス      ssu     ッズ      zzu     ッセ      sse     ッゼ      zze     ッソ      sso
ッゾ      zzo     ッタ      tta     ッダ      dda     ッチ      cchi    ッティ  tti
ッチャ     ccha    ッチュ     cchu    ッチョ     ccho    ッヂ      ddi
ッヂャ     ddya    ッヂュ     ddyu    ッヂョ     ddyo    ッツ      ttsu
ッヅ      ddu     ッテ      tte     ッデ      dde     ット      tto     ッド      ddo
ッドゥ  ddu
ッハ      hha     ッバ      bba     ッパ      ppa     ッヒ      hhi
ッヒャ     hhya    ッヒュ     hhyu    ッヒョ     hhyo    ッビ      bbi
ッビャ     bbya    ッビュ     bbyu    ッビョ     bbyo    ッピ      ppi
ッピャ     ppya    ッピュ     ppyu    ッピョ     ppyo    ッフ      ffu     ッフュ  ffu
ッファ     ffa     ッフィ     ffi     ッフェ     ffe     ッフォ     ffo
ッブ      bbu     ップ      ppu     ッヘ      hhe     ッベ      bbe     ッペ      ppe
ッホ      hho     ッボ      bbo     ッポ      ppo     ッヤ      yya     ッユ      yyu
ッヨ      yyo     ッラ      rra     ッリ      rri     ッリャ     rrya
ッリュ     rryu    ッリョ     rryo    ッル      rru     ッレ      rre
ッロ      rro

ツ       tsu     ヅ       du      テ       te      デ       de      ト       to
ド       do      ドゥ    du

ナ       na      ニ       ni      ニャ      nya     ニュ      nyu     ニョ      nyo
ヌ       nu      ネ       ne      ノ       no

ハ       ha      バ       ba      パ       pa      ヒ       hi      ヒャ      hya
ヒュ      hyu     ヒョ      hyo     ビ       bi      ビャ      bya     ビュ      byu
ビョ      byo     ピ       pi      ピャ      pya     ピュ      pyu     ピョ      pyo
フ       fu      ファ      fa      フィ      fi      フェ      fe      フォ      fo
フュ    fu
ブ       bu      プ       pu      ヘ       he      ベ       be      ペ       pe
ホ       ho      ボ       bo      ポ       po

マ       ma      ミ       mi      ミャ      mya     ミュ      myu     ミョ      myo
ム       mu      メ       me      モ       mo

ャ       xya     ヤ       ya      ュ       xyu     ユ       yu      ョ       xyo
ヨ       yo

ラ       ra      リ       ri      リャ      rya     リュ      ryu     リョ      ryo
ル       ru      レ       re      ロ       ro

ヮ       xwa     ワ       wa      ウィ    wi      ヰ wi      ヱ       we      ウェ    we
ヲ       wo      ウォ    wo      ン n

ン     n'
ディ   di
ー     -
チェ    che
ッチェ     cche
ジェ      je
"""

HEPBURNTAB_H = """ぁ      xa      あ      a      ぃ      xi      い      i      ぅ      xu
う      u      う゛      vu      う゛ぁ      va      う゛ぃ      vi      う゛ぇ      ve
う゛ぉ      vo      ぇ      xe      え      e      ぉ      xo      お      o


か      ka      が      ga      き      ki      きゃ      kya      きゅ      kyu
きょ      kyo      ぎ      gi      ぎゃ      gya      ぎゅ      gyu      ぎょ      gyo
く      ku      ぐ      gu      け      ke      げ      ge      こ      ko
ご      go

さ      sa      ざ      za      し      shi      しゃ      sha      しゅ      shu
しょ      sho      じ      ji      じゃ      ja      じゅ      ju      じょ      jo
す      su      ず      zu      せ      se      ぜ      ze      そ      so
ぞ      zo

た      ta      だ      da      ち      chi      ちゃ      cha      ちゅ      chu
ちょ      cho      ぢ      di      ぢゃ      dya      ぢゅ      dyu      ぢょ      dyo

っ      xtsu
っう゛      vvu      っう゛ぁ      vva      っう゛ぃ      vvi
っう゛ぇ      vve      っう゛ぉ      vvo
っか      kka      っが      gga      っき      kki      っきゃ      kkya
っきゅ      kkyu      っきょ      kkyo      っぎ      ggi      っぎゃ      ggya
っぎゅ      ggyu      っぎょ      ggyo      っく      kku      っぐ      ggu
っけ      kke      っげ      gge      っこ      kko      っご      ggo      っさ      ssa
っざ      zza      っし      sshi      っしゃ      ssha
っしゅ      sshu      っしょ      ssho
っじ      jji      っじゃ      jja      っじゅ      jju      っじょ      jjo
っす      ssu      っず      zzu      っせ      sse      っぜ      zze      っそ      sso
っぞ      zzo      った      tta      っだ      dda      っち      cchi
っちゃ      ccha      っちゅ      cchu      っちょ      ccho      っぢ      ddi
っぢゃ      ddya      っぢゅ      ddyu      っぢょ      ddyo      っつ      ttsu
っづ      ddu      って      tte      っで      dde      っと      tto      っど      ddo
っは      hha      っば      bba      っぱ      ppa      っひ      hhi
っひゃ      hhya      っひゅ      hhyu      っひょ      hhyo      っび      bbi
っびゃ      bbya      っびゅ      bbyu      っびょ      bbyo      っぴ      ppi
っぴゃ      ppya      っぴゅ      ppyu      っぴょ      ppyo      っふ      ffu
っふぁ      ffa      っふぃ      ffi      っふぇ      ffe      っふぉ      ffo
っぶ      bbu      っぷ      ppu      っへ      hhe      っべ      bbe      っぺ      ppe
っほ      hho      っぼ      bbo      っぽ      ppo      っや      yya      っゆ      yyu
っよ      yyo      っら      rra      っり      rri      っりゃ      rrya
っりゅ      rryu      っりょ      rryo      っる      rru      っれ      rre
っろ      rro

つ      tsu      づ      du      て      te      で      de      と      to
ど      do

な      na      に      ni      にゃ      nya      にゅ      nyu      にょ      nyo
ぬ      nu      ね      ne      の      no

は      ha      ば      ba      ぱ      pa      ひ      hi      ひゃ      hya
ひゅ      hyu      ひょ      hyo      び      bi      びゃ      bya      びゅ      byu
びょ      byo      ぴ      pi      ぴゃ      pya      ぴゅ      pyu      ぴょ      pyo
ふ      fu      ふぁ      fa      ふぃ      fi      ふぇ      fe      ふぉ      fo
ぶ      bu      ぷ      pu      へ      he      べ      be      ぺ      pe
ほ      ho      ぼ      bo      ぽ      po

ま      ma      み      mi      みゃ      mya      みゅ      myu      みょ      myo
む      mu      め      me      も      mo

ゃ      xya      や      ya      ゅ      xyu      ゆ      yu      ょ      xyo
よ      yo

ら      ra      り      ri      りゃ      rya      りゅ      ryu      りょ      ryo
る      ru      れ      re      ろ      ro

ゎ      xwa      わ      wa      ゐ      wi      ゑ      we
を      wo      ん      n

ん     n'
でぃ   dyi
ー     -
ちぇ    che
っちぇ      cche
じぇ      je
"""

def pairs(arr, size=2):
    for i in range(0, len(arr)-1, size):
        yield arr[i:i+size]



# Use Katakana

KANROM = {}
ROMKAN = {}

for pair in pairs(re.split("\s+", KUNREITAB + HEPBURNTAB)):
    kana, roma = pair
    KANROM[kana] = roma
    ROMKAN[roma] = kana

# special modification
# wo -> ヲ, but ヲ/ウォ -> wo
# du -> ヅ, but ヅ/ドゥ -> du
# we -> ウェ, ウェ -> we
ROMKAN.update( {"du": "ヅ", "di": "ヂ", "fu": "フ", "ti": "チ",
                "wi": "ウィ", "we": "ウェ", "wo": "ヲ" } )

# Sort in long order so that a longer Romaji sequence precedes.

_len_cmp = lambda x: -len(x)
ROMPAT = re.compile("|".join(sorted(ROMKAN.keys(), key=_len_cmp)) )

_kanpat_cmp = lambda x, y: (len(y) > len(x)) - (len(y) < len(x)) or (len(KANROM[x]) > len(KANROM[x])) - (len(KANROM[x]) < len(KANROM[x]))
KANPAT = re.compile("|".join(sorted(KANROM.keys(), key=cmp_to_key(_kanpat_cmp))))

KUNREI = [y for (x, y) in pairs(re.split("\s+", KUNREITAB)) ]
HEPBURN = [y for (x, y) in pairs(re.split("\s+", HEPBURNTAB) )]

KUNPAT = re.compile("|".join(sorted(KUNREI, key=_len_cmp)) )
HEPPAT = re.compile("|".join(sorted(HEPBURN, key=_len_cmp)) )

TO_HEPBURN = {}
TO_KUNREI = {}

for kun, hep in zip(KUNREI, HEPBURN):
    TO_HEPBURN[kun] = hep
    TO_KUNREI[hep] = kun

TO_HEPBURN.update( {'ti': 'chi' })

# Use Hiragana

KANROM_H = {}
ROMKAN_H = {}

for pair in pairs(re.split("\s+", KUNREITAB_H + HEPBURNTAB_H)):
    kana, roma = pair
    KANROM_H[kana] = roma
    ROMKAN_H[roma] = kana

# special modification
# wo -> ヲ, but ヲ/ウォ -> wo
# du -> ヅ, but ヅ/ドゥ -> du
# we -> ウェ, ウェ -> we
ROMKAN_H.update( {"du": "づ", "di": "ぢ", "fu": "ふ", "ti": "ち",
                "wi": "うぃ", "we": "うぇ", "wo": "を" } )

# Sort in long order so that a longer Romaji sequence precedes.

_len_cmp = lambda x: -len(x)
ROMPAT_H = re.compile("|".join(sorted(ROMKAN_H.keys(), key=_len_cmp)) )

_kanpat_cmp = lambda x, y: (len(y) > len(x)) - (len(y) < len(x)) or (len(KANROM_H[x]) > len(KANROM_H[x])) - (len(KANROM_H[x]) < len(KANROM_H[x]))
KANPAT_H = re.compile("|".join(sorted(KANROM_H.keys(), key=cmp_to_key(_kanpat_cmp))))

KUNREI_H = [y for (x, y) in pairs(re.split("\s+", KUNREITAB_H)) ]
HEPBURN_H = [y for (x, y) in pairs(re.split("\s+", HEPBURNTAB_H) )]

KUNPAT_H = re.compile("|".join(sorted(KUNREI_H, key=_len_cmp)) )
HEPPAT_H = re.compile("|".join(sorted(HEPBURN_H, key=_len_cmp)) )

TO_HEPBURN_H = {}
TO_KUNREI_H = {}

for kun, hep in zip(KUNREI_H, HEPBURN_H):
    TO_HEPBURN_H[kun] = hep
    TO_KUNREI_H[hep] = kun

TO_HEPBURN_H.update( {'ti': 'chi' })



def normalize_double_n(str):
    """
    Normalize double n.
    """

    # Replace double n with n'
    str = re.sub("nn", "n'", str)
    # Remove unnecessary apostrophes
    str = re.sub("n'(?=[^aiueoyn]|$)", "n", str)

    return str

def to_katakana(str):
    """
    Convert a Romaji (ローマ字) to a Katakana (片仮名).
    """

    str = str.lower()
    str = normalize_double_n(str)

    tmp = ROMPAT.sub(lambda x: ROMKAN[x.group(0)], str)
    return tmp

def to_hiragana(str):
    """
    Convert a Romaji (ローマ字) to a Hiragana (平仮名).
    """

    str = str.lower()
    str = normalize_double_n(str)

    tmp = ROMPAT_H.sub(lambda x: ROMKAN_H[x.group(0)], str)
    return tmp

def to_kana(str):
    """
    Convert a Romaji (ローマ字) to a Katakana (片仮名). (same as to_katakana)
    """

    return to_katakana(str)

def to_hepburn(str):
    """
    Convert a Kana (仮名) or a Kunrei-shiki Romaji (訓令式ローマ字) to a Hepburn Romaji (ヘボン式ローマ字).
    """

    tmp = str
    tmp = KANPAT.sub(lambda x: KANROM[x.group(0)], tmp)
    tmp = KANPAT_H.sub(lambda x: KANROM_H[x.group(0)], tmp)

    # Remove unnecessary apostrophes
    tmp = re.sub("n'(?=[^aeiuoyn]|$)", "n", tmp)

    # If unmodified, it's a Kunrei-shiki Romaji -- convert it to a Hepburn Romaji
    if tmp == str:
        tmp = tmp.lower()
        tmp = normalize_double_n(tmp)
        tmp = KUNPAT.sub(lambda x: TO_HEPBURN[x.group(0)], tmp)

    return tmp

def to_kunrei(str):
    """
    Convert a Kana (仮名) or a Hepburn Romaji (ヘボン式ローマ字) to a Kunrei-shiki Romaji (訓令式ローマ字).
    """

    tmp = str
    tmp = KANPAT.sub(lambda x: KANROM[x.group(0)], tmp)
    tmp = KANPAT_H.sub(lambda x: KANROM_H[x.group(0)], tmp)

    # Remove unnecessary apostrophes
    tmp = re.sub("n'(?=[^aeiuoyn]|$)", "n", tmp)

    # If unmodified, it's a Hepburn Romaji Romaji -- convert it to a Kunrei-shiki Romaji
    # If modified, it's also a Hepburn Romaji Romaji -- convert it to a Kunrei-shiki Romaji
    tmp = tmp.lower()
    tmp = normalize_double_n(tmp)
    tmp = HEPPAT.sub(lambda x: TO_KUNREI[x.group(0)], tmp)

    return tmp

def to_roma(str):
    """
    Convert a Kana (仮名) to a Hepburn Romaji (ヘボン式ローマ字).
    """

    tmp = str
    tmp = KANPAT.sub(lambda x: KANROM[x.group(0)], tmp)
    tmp = KANPAT_H.sub(lambda x: KANROM_H[x.group(0)], tmp)

    # Remove unnecessary apostrophes
    tmp = re.sub("n'(?=[^aeiuoyn]|$)", "n", tmp)

    return tmp

def is_consonant(str):
    """
    Return a MatchObject if a Latin letter is a consonant in Japanese.
    Return None otherwise.
    """

    str = str.lower()

    return re.match("[ckgszjtdhfpbmyrwxn]", str)

def is_vowel(str):
    """
    Return a MatchObject if a Latin letter is a vowel in Japanese.
    Return None otherwise.
    """

    str = str.lower()

    return re.match("[aeiou]", str)

def expand_consonant(str):
    """
    Expand consonant to its related moras.
    Example: 'sh' => ['sha', 'she', 'shi', 'sho', 'shu']
    """

    str = str.lower()

    return sorted([mora for mora in ROMKAN.keys() if re.match("^%s.$" % str, mora)])
