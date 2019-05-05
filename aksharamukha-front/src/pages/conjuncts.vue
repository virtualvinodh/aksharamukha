<template>
  <q-page padding>
<div class="row q-mt-sm">
<span class="q-mt-md"> Main: </span>
       <q-select
        filter
        inset
        lable="front"
        autofocus-filter
        filter-placeholder="search"
        placeholder="Input Script"
        v-model="script1"
        @input="compoundsGen"
        class="q-ma-sm col-md-3"
        :options="scriptsIndic"
      />
<span class="q-ml-md q-mt-md"> Guide: </span>
       <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        placeholder="Input Script"
        v-model="script2"
        @input="compoundsGen"
        class="q-ma-sm col-md-3"
        :options="scriptsOutput"
      />
<span class="q-ml-md q-mt-md"> Vowel: </span>
       <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        placeholder="Input Script"
        v-model="vowel"
        @input="compoundsGen"
        class="q-ma-sm col-md-1"
        :options="vowelOptions"
      />

      <q-option-group
        color="dark"
        type="checkbox"
        class="col-xs-12 col-lg-3 q-ml-xl q-mr-md"
        v-model="postOptionCon"
        @input="compoundsGen"
        :options="typeof conjunctsOptions[script1] !== 'undefined' ? conjunctsOptions[script1] : []"
      />
      <!-- <q-toggle color="dark" v-model="conjunctsShow" label="Include conjuncts" class="q-ml-sm q-mb-sm q-mt-sm"/> -->

</div>
<div class="q-body-1 q-mt-lg">Select a script to view all possible conjuncts associated with the script. The below may be empty, if the script does not have a way to denote conjuncts, such as the lack of Virama and/or final consonants.</div>
      <h5>Final Consonants <q-spinner-comment color="dark" :size="30" v-show="loading"/> </h5>
      <span v-for="(conjunct, index) in conjuncts1S1" :key="conjunct+index + 'a'">
         <learncard :script1="script1" :text1="conjunct" :script2="script2" :text2="conjuncts1S2[index]"> </learncard>
      </span>

      <p class="q-mt-xl">Below listed are 807 Sanskrit conjuncts as enumerated <a href="http://www.sanskritweb.net/sansdocs/mathe.pdf">here</a> ( + few Pali conjuncts) </p>
      <h5> 2 Consonants </h5>
      <span v-for="(conjunct, index) in conjuncts2S1" :key="conjunct+index + 'a1'">
         <learncard :script1="script1" :text1="conjunct" :script2="script2" :text2="conjuncts2S2[index]"> </learncard>
      </span>

      <h5> 3 Consonants </h5>
      <span v-for="(conjunct, index) in conjuncts3S1" :key="conjunct+index + 'a2'">
         <learncard :script1="script1" :text1="conjunct" :script2="script2" :text2="conjuncts3S2[index]"> </learncard>
      </span>

      <h5> 4 Consonants </h5>
      <span v-for="(conjunct, index) in conjuncts4S1" :key="conjunct+index + 'a3'">
         <learncard :script1="script1" :text1="conjunct" :script2="script2" :text2="conjuncts4S2[index]"> </learncard>
      </span>

      <h5> 5 Consonants </h5>
      <span v-for="(conjunct, index) in conjuncts5S1" :key="conjunct+index + 'a4'">
         <learncard :script1="script1" :text1="conjunct" :script2="script2" :text2="conjuncts5S2[index]"> </learncard>
      </span>
  </q-page>
</template>

<style>
</style>

<script>
import Learncard from '../components/Learncard'
import Transliterate from '../components/Transliterate'
import {ScriptMixin} from '../mixins/ScriptMixin'
import {QPageSticky, QSelect, QOptionGroup, QSpinnerComment} from 'quasar'

var _ = require('underscore')
console.log(_)

export default {
  name: 'PageIndex',
  mixins: [ScriptMixin],
  components: {
    QPageSticky,
    Transliterate,
    Learncard,
    QSelect,
    QSpinnerComment,
    QOptionGroup
  },
  data () {
    return {
      options: {script: 'Devanagari', sourcePreserve: false},
      conjunctsOptions:
        { 'Sinhala':
          [
            { label: 'Enable all conjuncts',
              value: 'SinhalaConjuncts'
            }
          ],
        'Chakma':
          [
            { label: 'Enable all conjuncts',
              value: 'ChakmaEnableAllConjuncts'
            }
          ]
        },
      postOptionCon: ['SinhalaConjuncts', 'ChakmaEnableAllConjuncts'],
      vowel: 'a',
      text: '',
      script1: '',
      script2: 'IAST',
      conjuncts5: 'rtsny'.split(',').map(x => x.trim()),
      conjuncts4: 'ktry, ktvy, kṣṇy, kṣmy, kstr, gdvy, gdhry, ṅkty, ṅktr, ṅktv, ṅkṣṇ, ṅkṣm, ṅkṣy, ṅkṣv, ṅgdhy, ṅgdhv, ṅghry, tkṣm, tkṣv, ttry, tstr, tsthy, tspr, tsphy, ddvy, nttv, ntry, ntvy, ntst, ntsth, ntsn, ntsp, ntsy, ntsr, ntsv, nddhy, nddhv, ndry, ndvy, ndhry, nstr, nsphy, ptry, psny, rkṣṇ, rkṣy, rksv, rṅgy, rjmy, rttr, rtny, rtry, rtvy, rtsn, rtsy, rddhy, rdry, rdvy, rdhny, rśvy, rṣṭy, rṣṇy, lgvy, ṣṭry, stry, sthny'.split(',').map(x => x.trim()),
      conjuncts3: 'kkr, kkl, kkv, kkṣ, kty, ktr, ktv, kthn, kthy, kny,kpr, kpl, kmy, kry, kly, kśm, kśr, kśl, kśv, kṣṇ, kṣm, kṣy, kṣr, kṣv, kst, ksth, ksn, ksp, ksph, ksm, ksy, ksr, ksv, ggr, gghy, gghr, gjñ, gjy, gjv, gdy, gdr, gdv, gdhy, gdhr, gdhv, gny, gbr, gbhy, gbhr, gmy, gry, grv, gvy, gvr, ghny, ghry, ghvy, ṅkt, ṅkth, ṅky, ṅkr, ṅkl, ṅkv, ṅkṣ, ṅks, ṅkhy, ṅgdh, ṅgy, ṅgr, ṅgv, ṅghn, ṅghy, ṅghr, ṅtr, ṅtv, ṅdhy, ṅny, ṅnr, ṅpr, ṅvy, ṅvr, ṅsv, ccy, cchm, cchy, cchr, cchl, cchv, cñy, jjñ, jjy, jjv, jjhy, jñy, jñv, jmy, jry, jvy, ñcm, ñcy, ñcv, ñchn, ñchy, ñchr, ñchl, ñchv, ñjñ, ñjm, ñjy, ñjv, ñśm, ñśy, ñśr, ñśl, ñśv, ṭkr, ṭkṣ, ṭṭy, ṭtr, ṭtv, ṭpr, ṭśr, ṭśl, ṭst, ṭsth, ṭsn, ṭsp, ṭsv, ḍgy, ḍgr, ḍghr, ḍjñ, ḍjy, ḍḍhy, ḍḍhv, ḍdv, ḍbr, ḍbhy, ḍbhr, ḍvy, ṇṭy, ṇṭhy, ṇḍḍh, ṇḍy, ṇḍr, ṇḍv, ṇḍhy, ṇḍhr, ṇvy, tky, tkr, tkl, tkv, tkṣ, tkhy, ttn, ttm, tty, ttr, ttv, tts, tthy, tny, tnv, tpr, tpl, tmy, tyv, try, trv, tvy, tsk, tskh, tst, tsth, tsn, tsp, tsph, tsm, tsy, tsr, tsv, thny, thvy, dgr, dgl, dghn, dghr, ddy, ddr, ddv, ddhm, ddhy, ddhr, ddhv, dbr, dbhy, dbhr, dbhv, dmy, dry, drv, dvy, dvr, dhny, dhry, dhvy, dhvr, nkr, nkl, nkv, nkṣ, nkhy, ngr, ngl, nghn, nghr, ntt, ntth, ntm, nty, ntr, ntv, nts, nthy, nddh, ndm, ndy, ndr, ndv, ndhm, ndhy, ndhr, ndhv, nny, nnv, npr, npl, nps, nbr, nbhr, nmy, nmr, nml, nyv, nvy, nvr, nsk, nskh, nst, nsth, nsn, nsp, nsph, nsm, nsy, nsr, nsv, nhy, nhr, nhv, pkṣ, pty, ptr, ptv, pny, ppr, pry, pśy, psn, psy, psv, bgr, bjy, bdy, bdhy, bdhv, bbr, bbhy, bvy, bhry, bhrv, bhvy, mny, mpy, mpr, mpl, mps, mby, mbr, mbv, mbhy, mbhr, mmy, mmr, mml, mry, rkc, rkt, rkth, rkp, rky, rkṣ, rks, rkhy, rgg, rggh, rgj, rgbh, rgy, rgr, rgl, rgv, rghn, rghy, rghr, rṅkh, rṅg, rcch, rcy, rjñ, rjm, rjy, rjv, rñj, rḍy, rḍhy, rṇṇ, rṇy, rṇv, rtt, rtn, rtm, rty, rtr, rtv, rts, rthy, rddh, rdm, rdy, rdr, rdv, rdhn, rdhm, rdhy, rdhr, rdhv, rny, rnv, rpy, rbr, rbhy, rbhr, rbhv, rmy, rmr, rml, ryy, rvy, rvr, rvl, rśm, rśy, rśv, rṣṭ, rṣṭh, rṣṇ, rṣm, rṣy, rṣv, rsr, rsv, rhy, rhr, rhl, rhv, lky, lgv, lpy, lby, lbhy, lly, lvy, lhy, vny, ścy, śny, śmy, śry, śrv, śvy, ṣky, ṣkr, ṣkl, ṣkv, ṣkṣ, ṣṭy, ṣṭr, ṣṭv, ṣṭhy, ṣṭhv, ṣṇy, ṣṇv, ṣpy, ṣpr, ṣpl, ṣmy, skr, stm, sty, str, stv, sts, sthn, sthy, sny, spr, sphy, smy, sry, svy, ssy, ssv, hny, hmy, hvy'.split(',').map(x => x.trim()),
      conjuncts2: 'kk, kkh, kc, kch, kṇ, kt, kth, kn, kp, kph, km, ky, kr, kl, kv, kś, kṣ, ks, khkh, khn, khy, khv, gg, ggh, gj, gḍ, gṇ, gd, gdh, gn, gb, gbh, gm, gy, gr, gl, gv, ghn, ghm, ghy, ghr, ghv, ṅk, ṅkh, ṅg, ṅgh, ṅṅ, ṅc, ṅj, ṅt, ṅd, ṅdh, ṅn, ṅp, ṅbh, ṅm, ṅy, ṅr, ṅv, ṅś, ṅs, ṅh, cc, cch, cñ, cm, cy, cr, cv, chy, jj, jjh, jñ, jm, jy, jr, jv, jh, jhñ, cñ, ch, ñj, ñjh, ññ, ñś, ñh, ṭk, ṭkh, ṭc, ṭch, ṭṭ, ṭṇ, ṭt, ṭp, ṭph, ṭm, ṭy, ṭv, ṭś, ṭṣ, ṭs, ṭhy, ḍg, ḍgh, ḍj, ḍḍ, ḍḍh, ḍd, ḍdh, ḍb, ḍbh, ḍm, ḍy, ḍr, ḍl, ḍv, ḍhy, ḍhr, ḍhv, ṇṭ, ṇṭh, ṇḍ, ṇḍh, ṇṇ, ṇn, ṇm, ṇy, ṇv, ṇh, tk, tkh, tt, tth, tn, tp, tph, tm, ty, tr, tv, tṣ, ts, thn, thy, thr, thv, dg, dgh, dd, ddh, dn, db, dbh, dm, dy, dr, dv, dhn, dhm, dhy, dhr, dhv, nk, nkh, ng, ngh, nt, nth, nd, ndh, nn, np, nph, nb, nbh, nm, ny, nr, nv, nṣ, ns, nh, pk, pkh, pc, pch, pṭ, pṇ, pt, pn, pp, pph, pm, py, pr, pl, pv, pś, ps, bg, bj, bd, bdh, bb, bbh, by, br, bl, bv, bhṇ, bhn, bhm, bhy, bhr, bhl, bhv, mṇ, mn, mp, mph, mb, mbh, mm, my, mr, ml, mv, mh, yy, yv, rk, rk, hr, gr, gh, rc, rch, rj, rj, hr, ṭr, ḍr, ḍh, rṇ, rt, rth, rd, rdh, rn, rp, rph, rb, rbh, rm, ry, rl, rv, rś, rṣ, rs, rh, lk, lg, ld, lp, lph, lb, lbh, lm, ly, ll, lv, lś, lh, vṇ, vn, vy, vr, vl, śc, śch, śn, śp, śm, śy, śr, śl, śv, śś, ṣk, ṣkh, ṣṭ, ṣṭh, ṣṇ, ṣp, ṣph, ṣm, ṣy, ṣr, ṣv, ṣṣ, sk, skh, st, sth, sn, sp, sph, sm, sy, sr, sv, ss, hṇ, hn, hm, hy, hr, hl, hv, l̤h'.split(',').map(x => x.trim()),
      conjuncts1: [],
      conjuncts2S1: [],
      conjuncts2S2: [],
      conjuncts3S1: [],
      conjuncts3S2: [],
      conjuncts4S1: [],
      conjuncts4S2: [],
      conjuncts5S1: [],
      conjuncts5S2: [],
      conjuncts1S1: [],
      conjuncts1S2: [],
      vowelOptions: [],
      loading: false
    }
  },
  watch: {
    options: function () {
      this.compoundsGen()
    }
  },
  mounted: async function () {
    // this.script1 = this.scriptRandom().value

    var vowelsIAST = ['a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'ĕ', 'e', 'ai', 'ŏ', 'o', 'au', 'aṃ', 'aḥ']
    vowelsIAST.forEach(function (vowel) {
      this.vowelOptions.push({label: vowel, value: vowel})
    }.bind(this))
    // this.compoundsGen()
  },
  methods: {
    compoundsGen: async function () {
      this.loading = true

      /*
      var finCons = ['k', 'kh', 'g', 'gh', 'ṅ', 'c', 'ch', 'j', 'jh', 'ñ', 'ṭ', 'ṭh', 'ḍ', 'ḍh', 'ṇ', 't', 'th', 'd', 'dh', 'n', 'p', 'ph', 'b', 'bh', 'm', 'y', 'r', 'l', 'v', 'ś', 'ṣ', 's', 'h', 'l̤']

      finCons.forEach(function (char) {
        this.conjuncts1.push(this.vowel + char)
      }.bind(this))

      var conjAll = {}

      for (var i = 1; i <= 5; i++) {
        console.log(i)
        var conjunctsV = 'conjuncts' + i
        var conjunctsVS1 = conjunctsV + 'S1'
        var conjunctsa

        if (i !== 1) {
          conjunctsa = this[conjunctsV].map(x => x + this.vowel)
        } else {
          conjunctsa = this[conjunctsV]
        }

        conjAll[conjunctsVS1] = conjunctsa
      }

      */

      var data = {
        vowel: this.vowel,
        script1: this.script1,
        script2: this.script2,
        postoptions: this.postOptionCon
      }
      var dhis = this
      this.apiCall.post('/conjuncts', data)
        .then(function (response) {
          for (var key in response.data) {
            dhis[key] = response.data[key]
          }
          dhis.loading = false
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
