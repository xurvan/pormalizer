import re
import unicodedata


class Pormalizer:
    valid_chars: list
    replace_map: dict

    def __init__(self):
        self.valid_chars = [
            '\u0627',  # ARABIC LETTER ALEF
            '\u0628',  # ARABIC LETTER BEH
            '\u062A',  # ARABIC LETTER TEH
            '\u062B',  # ARABIC LETTER THEH
            '\u062C',  # ARABIC LETTER JEEM
            '\u062D',  # ARABIC LETTER HAH
            '\u062E',  # ARABIC LETTER KHAH
            '\u062F',  # ARABIC LETTER DAL
            '\u0630',  # ARABIC LETTER THAL
            '\u0631',  # ARABIC LETTER REH
            '\u0632',  # ARABIC LETTER ZAIN
            '\u0633',  # ARABIC LETTER SEEN
            '\u0634',  # ARABIC LETTER SHEEN
            '\u0635',  # ARABIC LETTER SAD
            '\u0636',  # ARABIC LETTER DAD
            '\u0637',  # ARABIC LETTER TAH
            '\u0638',  # ARABIC LETTER ZAH
            '\u0639',  # ARABIC LETTER AIN
            '\u063A',  # ARABIC LETTER GHAIN
            '\u0641',  # ARABIC LETTER FEH
            '\u0642',  # ARABIC LETTER QAF
            '\u06A9',  # ARABIC LETTER KEHEH
            '\u0644',  # ARABIC LETTER LAM
            '\u0645',  # ARABIC LETTER MEEM
            '\u0646',  # ARABIC LETTER NOON
            '\u0647',  # ARABIC LETTER HEH
            '\u0648',  # ARABIC LETTER WAW
            '\u067E',  # ARABIC LETTER PEH
            '\u0686',  # ARABIC LETTER TCHEH
            '\u0698',  # ARABIC LETTER JEH
            '\u06AF',  # ARABIC LETTER GAF
            '\u06CC',  # ARABIC LETTER FARSI YEH
            '\u0030',  # DIGIT ZERO
            '\u0031',  # DIGIT ONE
            '\u0032',  # DIGIT TWO
            '\u0033',  # DIGIT THREE
            '\u0034',  # DIGIT FOUR
            '\u0035',  # DIGIT FIVE
            '\u0036',  # DIGIT SIX
            '\u0037',  # DIGIT SEVEN
            '\u0038',  # DIGIT EIGHT
            '\u0039',  # DIGIT NINE
        ]
        self.replace_map = {
            '\u0660': '\u0030',  # ARABIC-INDIC DIGIT ZERO
            '\u0661': '\u0031',  # ARABIC-INDIC DIGIT ONE
            '\u0662': '\u0032',  # ARABIC-INDIC DIGIT TWO
            '\u0663': '\u0033',  # ARABIC-INDIC DIGIT THREE
            '\u0664': '\u0034',  # ARABIC-INDIC DIGIT FOUR
            '\u0665': '\u0035',  # ARABIC-INDIC DIGIT FIVE
            '\u0666': '\u0036',  # ARABIC-INDIC DIGIT SIX
            '\u0667': '\u0037',  # ARABIC-INDIC DIGIT SEVEN
            '\u0668': '\u0038',  # ARABIC-INDIC DIGIT EIGHT
            '\u0669': '\u0039',  # ARABIC-INDIC DIGIT NINE
            '\u06F0': '\u0030',  # EXTENDED ARABIC-INDIC DIGIT ZERO
            '\u06F1': '\u0031',  # EXTENDED ARABIC-INDIC DIGIT ONE
            '\u06F2': '\u0032',  # EXTENDED ARABIC-INDIC DIGIT TWO
            '\u06F3': '\u0033',  # EXTENDED ARABIC-INDIC DIGIT THREE
            '\u06F4': '\u0034',  # EXTENDED ARABIC-INDIC DIGIT FOUR
            '\u06F5': '\u0035',  # EXTENDED ARABIC-INDIC DIGIT FIVE
            '\u06F6': '\u0036',  # EXTENDED ARABIC-INDIC DIGIT SIX
            '\u06F7': '\u0037',  # EXTENDED ARABIC-INDIC DIGIT SEVEN
            '\u06F8': '\u0038',  # EXTENDED ARABIC-INDIC DIGIT EIGHT
            '\u06F9': '\u0039',  # EXTENDED ARABIC-INDIC DIGIT NINE
            '\u0643': '\u06A9',  # ARABIC LETTER KAF
            '\u063B': '\u06A9',  # ARABIC LETTER KEHEH WITH TWO DOTS ABOVE
            '\u063C': '\u06A9',  # ARABIC LETTER KEHEH WITH THREE DOTS BELOW
            '\u06AA': '\u06A9',  # ARABIC LETTER SWASH KAF
            '\u06AB': '\u06A9',  # ARABIC LETTER KAF WITH RING
            '\u06AC': '\u06A9',  # ARABIC LETTER KAF WITH DOT ABOVE
            '\u06AD': '\u06A9',  # ARABIC LETTER NG
            '\u06AE': '\u06A9',  # ARABIC LETTER KAF WITH THREE DOTS BELOW
            '\u0762': '\u06A9',  # ARABIC LETTER KEHEH WITH DOT ABOVE
            '\u0763': '\u06A9',  # ARABIC LETTER KEHEH WITH THREE DOTS ABOVE
            '\u0764': '\u06A9',  # ARABIC LETTER KEHEH WITH THREE DOTS POINTING UPWARDS BELOW
            '\u077F': '\u06A9',  # ARABIC LETTER KAF WITH TWO DOTS ABOVE
            '\u08B4': '\u06A9',  # ARABIC LETTER KAF WITH DOT BELOW
            '\u0620': '\u06CC',  # ARABIC LETTER KASHMIRI YEH
            '\u0649': '\u06CC',  # ARABIC LETTER ALEF MAKSURA
            '\u064A': '\u06CC',  # ARABIC LETTER YEH
            '\u0626': '\u06CC',  # ARABIC LETTER YEH WITH HAMZA ABOVE
            '\u063D': '\u06CC',  # ARABIC LETTER FARSI YEH WITH INVERTED V
            '\u063E': '\u06CC',  # ARABIC LETTER FARSI YEH WITH TWO DOTS ABOVE
            '\u063F': '\u06CC',  # ARABIC LETTER FARSI YEH WITH THREE DOTS ABOVE
            '\u0678': '\u06CC',  # ARABIC LETTER HIGH HAMZA YEH
            '\u06CD': '\u06CC',  # ARABIC LETTER YEH WITH TAIL
            '\u06CE': '\u06CC',  # ARABIC LETTER YEH WITH SMALL V
            '\u06D0': '\u06CC',  # ARABIC LETTER E
            '\u06D1': '\u06CC',  # ARABIC LETTER YEH WITH THREE DOTS BELOW
            '\u06D2': '\u06CC',  # ARABIC LETTER YEH BARREE
            '\u06D3': '\u06CC',  # ARABIC LETTER YEH BARREE WITH HAMZA ABOVE
            '\u08A8': '\u06CC',  # ARABIC LETTER YEH WITH TWO DOTS BELOW AND HAMZA ABOVE
            '\u08A9': '\u06CC',  # ARABIC LETTER YEH WITH TWO DOTS BELOW AND DOT ABOVE
            '\u06D5': '\u0647',  # ARABIC LETTER AE
            '\u06C0': '\u0647',  # ARABIC LETTER HEH WITH YEH ABOVE
            '\u06BE': '\u0647',  # ARABIC LETTER HEH DOACHASHMEE
            '\u06C1': '\u0647',  # ARABIC LETTER HEH GOAL
            '\u0624': '\u0648',  # ARABIC LETTER WAW WITH HAMZA ABOVE
            '\u0623': '\u0627',  # ARABIC LETTER ALEF WITH HAMZA ABOVE
            '\u0625': '\u0627',  # ARABIC LETTER ALEF WITH HAMZA BELOW
            '\u0629': '\u0647',  # ARABIC LETTER TEH MARBUTA
            '\uFE8E': '\u0627',  # ARABIC LETTER ALEF FINAL FORM
            '\uFE8D': '\u0627',  # ARABIC LETTER ALEF ISOLATED FORM
            '\uFEA9': '\u062F',  # ARABIC LETTER DAL ISOLATED FORM
            '\uFEAE': '\u0631',  # ARABIC LETTER REH FINAL FORM
            '\uFE91': '\u0628',  # ARABIC LETTER BEH INITIAL FORM
            '\uFEAD': '\u0631',  # ARABIC LETTER REH ISOLATED FORM
            '\u067A': '\u062A',  # ARABIC LETTER TTEHEH
            '\uFEE3': '\u0645',  # ARABIC LETTER MEEM INITIAL FORM
            '\uFEAA': '\u062F',  # ARABIC LETTER DAL FINAL FORM
            '\uFEEA': '\u0647',  # ARABIC LETTER HEH FINAL FORM
            '\uFEEE': '\u0648',  # ARABIC LETTER WAW FINAL FORM
            '\uFEE7': '\u0646',  # ARABIC LETTER NOON INITIAL FORM
            '\uFEED': '\u0648',  # ARABIC LETTER WAW ISOLATED FORM
            '\uFBFF': '\u06CC',  # ARABIC LETTER FARSI YEH MEDIAL FORM
            '\uFBFE': '\u06CC',  # ARABIC LETTER FARSI YEH INITIAL FORM
            '\uFBFD': '\u06CC',  # ARABIC LETTER FARSI YEH FINAL FORM
            '\uFEE8': '\u0646',  # ARABIC LETTER NOON MEDIAL FORM
            '\uFEB3': '\u0633',  # ARABIC LETTER SEEN INITIAL FORM
            '\uFEEB': '\u0647',  # ARABIC LETTER HEH INITIAL FORM
            '\uFEE5': '\u0646',  # ARABIC LETTER NOON ISOLATED FORM
            '\uFEAF': '\u0632',  # ARABIC LETTER ZAIN ISOLATED FORM
            '\uFE96': '\u062A',  # ARABIC LETTER TEH FINAL FORM
            '\uFEB7': '\u0634',  # ARABIC LETTER SHEEN INITIAL FORM
            '\uFB90': '\u06A9',  # ARABIC LETTER KEHEH INITIAL FORM
            '\uFE98': '\u062A',  # ARABIC LETTER TEH MEDIAL FORM
            '\uFEE4': '\u0645',  # ARABIC LETTER MEEM MEDIAL FORM
            '\uFE97': '\u062A',  # ARABIC LETTER TEH INITIAL FORM
            '\uFEA7': '\u062E',  # ARABIC LETTER KHAH INITIAL FORM
            '\uFBFC': '\u06CC',  # ARABIC LETTER FARSI YEH ISOLATED FORM
            '\uFEE6': '\u0646',  # ARABIC LETTER NOON FINAL FORM
            '\uFEE2': '\u0645',  # ARABIC LETTER MEEM FINAL FORM
            '\uFEE9': '\u0647',  # ARABIC LETTER HEH ISOLATED FORM
            '\uFEB4': '\u0633',  # ARABIC LETTER SEEN MEDIAL FORM
            '\uFB94': '\u06AF',  # ARABIC LETTER GAF INITIAL FORM
            '\uFECB': '\u0639',  # ARABIC LETTER AIN INITIAL FORM
            '\uFEB8': '\u0634',  # ARABIC LETTER SHEEN MEDIAL FORM
            '\uFEDF': '\u0644',  # ARABIC LETTER LAM INITIAL FORM
            '\uFE81': '\u0627',  # ARABIC LETTER ALEF WITH MADDA ABOVE ISOLATED FORM
            '\uFED3': '\u0641',  # ARABIC LETTER FEH INITIAL FORM
            '\uFEE1': '\u0645',  # ARABIC LETTER MEEM ISOLATED FORM
            '\uFE92': '\u0628',  # ARABIC LETTER BEH MEDIAL FORM
            '\uFEE0': '\u0644',  # ARABIC LETTER LAM MEDIAL FORM
            '\uFEA3': '\u062D',  # ARABIC LETTER HAH INITIAL FORM
            '\uFEF4': '\u06CC',  # ARABIC LETTER YEH MEDIAL FORM
            '\uFB95': '\u06AF',  # ARABIC LETTER GAF MEDIAL FORM
            '\uFB58': '\u067E',  # ARABIC LETTER PEH INITIAL FORM
            '\uFEEC': '\u0647',  # ARABIC LETTER HEH MEDIAL FORM
            '\u06B9': '\u0646',  # ARABIC LETTER NOON WITH DOT BELOW
            '\uFE9F': '\u062C',  # ARABIC LETTER JEEM INITIAL FORM
            '\uFB7C': '\u0686',  # ARABIC LETTER TCHEH INITIAL FORM
            '\uFED7': '\u0642',  # ARABIC LETTER QAF INITIAL FORM
            '\uFB91': '\u06A9',  # ARABIC LETTER KEHEH MEDIAL FORM
            '\uFEF3': '\u06CC',  # ARABIC LETTER YEH INITIAL FORM
            '\uFEB0': '\u0632',  # ARABIC LETTER ZAIN FINAL FORM
            '\uFED8': '\u0642',  # ARABIC LETTER QAF MEDIAL FORM
            '\uFECC': '\u0639',  # ARABIC LETTER AIN MEDIAL FORM
            '\uFED4': '\u0641',  # ARABIC LETTER FEH MEDIAL FORM
            '\uFEDD': '\u0644',  # ARABIC LETTER LAM ISOLATED FORM
            '\uFE95': '\u062A',  # ARABIC LETTER TEH ISOLATED FORM
            '\uFEDB': '\u06A9',  # ARABIC LETTER KAF INITIAL FORM
            '\uFEA8': '\u062E',  # ARABIC LETTER KHAH MEDIAL FORM
            '\uFEA0': '\u062C',  # ARABIC LETTER JEEM MEDIAL FORM
            '\uFEDE': '\u0644',  # ARABIC LETTER LAM FINAL FORM
            '\uFEB6': '\u0634',  # ARABIC LETTER SHEEN FINAL FORM
            '\uFEFC': '\u0644',  # ARABIC LIGATURE LAM WITH ALEF FINAL FORM
            '\uFEB5': '\u0634',  # ARABIC LETTER SHEEN ISOLATED FORM
            '\uFE8F': '\u0628',  # ARABIC LETTER BEH ISOLATED FORM
            '\u0671': '\u0627',  # ARABIC LETTER ALEF WASLA
            '\u0769': '\u0646',  # ARABIC LETTER NOON WITH SMALL V
            '\uFB8F': '\u06A9',  # ARABIC LETTER KEHEH FINAL FORM
            '\uFEBB': '\u0635',  # ARABIC LETTER SAD INITIAL FORM
            '\uFEF2': '\u06CC',  # ARABIC LETTER YEH FINAL FORM
            '\u060F': '\u0639',  # ARABIC SIGN MISRA
            '\uFEA4': '\u062D',  # ARABIC LETTER HAH MEDIAL FORM
            '\uFEF0': '\u06CC',  # ARABIC LETTER ALEF MAKSURA FINAL FORM
            '\u0767': '\u0646',  # ARABIC LETTER NOON WITH TWO DOTS BELOW
            '\uFECF': '\u063A',  # ARABIC LETTER GHAIN INITIAL FORM
            '\uFE90': '\u0628',  # ARABIC LETTER BEH FINAL FORM
            '\uFEC4': '\u0637',  # ARABIC LETTER TAH MEDIAL FORM
            '\uFEC3': '\u0637',  # ARABIC LETTER TAH INITIAL FORM
            '\uFED6': '\u0642',  # ARABIC LETTER QAF FINAL FORM
            '\uFEB2': '\u0633',  # ARABIC LETTER SEEN FINAL FORM
            '\uFEFB': '\u0644',  # ARABIC LIGATURE LAM WITH ALEF ISOLATED FORM
            '\uFEAC': '\u0630',  # ARABIC LETTER THAL FINAL FORM
            '\uFEBC': '\u0635',  # ARABIC LETTER SAD MEDIAL FORM
            '\u06C2': '\u0647',  # ARABIC LETTER HEH GOAL WITH HAMZA ABOVE
            '\uFEB1': '\u0633',  # ARABIC LETTER SEEN ISOLATED FORM
            '\u06B8': '\u0644',  # ARABIC LETTER LAM WITH THREE DOTS BELOW
            '\uFEDC': '\u06A9',  # ARABIC LETTER KAF MEDIAL FORM
            '\uFB7D': '\u0686',  # ARABIC LETTER TCHEH MEDIAL FORM
            '\uFEC0': '\u0636',  # ARABIC LETTER DAD MEDIAL FORM
            '\uFEF1': '\u06CC',  # ARABIC LETTER YEH ISOLATED FORM
            '\uFB93': '\u06AF',  # ARABIC LETTER GAF FINAL FORM
            '\uFEC8': '\u0638',  # ARABIC LETTER ZAH MEDIAL FORM
            '\uFED2': '\u0641',  # ARABIC LETTER FEH FINAL FORM
            '\uFEEF': '\u06CC',  # ARABIC LETTER ALEF MAKSURA ISOLATED FORM
            '\uFE8B': '\u06CC',  # ARABIC LETTER YEH WITH HAMZA ABOVE INITIAL FORM
            '\u076A': '\u0644',  # ARABIC LETTER LAM WITH BAR
            '\uFED5': '\u0642',  # ARABIC LETTER QAF ISOLATED FORM
            '\uFEC2': '\u0637',  # ARABIC LETTER TAH FINAL FORM
            '\uFBA9': '\u0647',  # ARABIC LETTER HEH GOAL MEDIAL FORM
            '\u06BA': '\u0646',  # ARABIC LETTER NOON GHUNNA
            '\uFEBF': '\u0636',  # ARABIC LETTER DAD INITIAL FORM
            '\u08AA': '\u0631',  # ARABIC LETTER REH WITH LOOP
            '\uFED1': '\u0641',  # ARABIC LETTER FEH ISOLATED FORM
            '\uFED0': '\u063A',  # ARABIC LETTER GHAIN MEDIAL FORM
            '\uFB8E': '\u06A9',  # ARABIC LETTER KEHEH ISOLATED FORM
            '\uFB59': '\u067E',  # ARABIC LETTER PEH MEDIAL FORM
            '\uFB7B': '\u0686',  # ARABIC LETTER TCHEH FINAL FORM
            '\u06C6': '\u0648',  # ARABIC LETTER OE
            '\uFECA': '\u0639',  # ARABIC LETTER AIN FINAL FORM
            '\u06C5': '\u0648',  # ARABIC LETTER KIRGHIZ OE
            '\u06B1': '\u06AF',  # ARABIC LETTER NGOEH
            '\uFE9D': '\u062C',  # ARABIC LETTER JEEM ISOLATED FORM
            '\uFE9C': '\u062B',  # ARABIC LETTER THEH MEDIAL FORM
            '\uFEAB': '\u0630',  # ARABIC LETTER THAL ISOLATED FORM
            '\u0672': '\u0627',  # ARABIC LETTER ALEF WITH WAVY HAMZA ABOVE
            '\uFB92': '\u06AF',  # ARABIC LETTER GAF ISOLATED FORM
            '\uFEC7': '\u0638',  # ARABIC LETTER ZAH INITIAL FORM
            '\u067C': '\u062A',  # ARABIC LETTER TEH WITH RING
            '\uFB8B': '\u0698',  # ARABIC LETTER JEH FINAL FORM
            '\uFE9E': '\u062C',  # ARABIC LETTER JEEM FINAL FORM
            '\u0691': '\u0631',  # ARABIC LETTER RREH
            '\uFEDA': '\u06A9',  # ARABIC LETTER KAF FINAL FORM
            '\uFECD': '\u063A',  # ARABIC LETTER GHAIN ISOLATED FORM
            '\uFEC9': '\u0639',  # ARABIC LETTER AIN ISOLATED FORM
            '\u06C3': '\u0647',  # ARABIC LETTER TEH MARBUTA GOAL
            '\uFEA2': '\u062D',  # ARABIC LETTER HAH FINAL FORM
            '\u0753': '\u062A',  # ARABIC LETTER BEH WITH THREE DOTS POINTING UPWARDS BELOW AND TWO DOTS ABOVE
            '\u06B5': '\u0644',  # ARABIC LETTER LAM WITH SMALL V
            '\uFEB9': '\u0635',  # ARABIC LETTER SAD ISOLATED FORM
            '\uFE83': '\u0627',  # ARABIC LETTER ALEF WITH HAMZA ABOVE ISOLATED FORM
            '\uFE8C': '\u06CC',  # ARABIC LETTER YEH WITH HAMZA ABOVE MEDIAL FORM
            '\uFEA1': '\u062D',  # ARABIC LETTER HAH ISOLATED FORM
            '\uFEA6': '\u062E',  # ARABIC LETTER KHAH FINAL FORM
            '\uFEC1': '\u0637',  # ARABIC LETTER TAH ISOLATED FORM
            '\uFE84': '\u0627',  # ARABIC LETTER ALEF WITH HAMZA ABOVE FINAL FORM
            '\uFEBD': '\u0636',  # ARABIC LETTER DAD ISOLATED FORM
            '\u0675': '\u0627',  # ARABIC LETTER HIGH HAMZA ALEF
            '\uFE9A': '\u062B',  # ARABIC LETTER THEH FINAL FORM
            '\uFBA7': '\u0647',  # ARABIC LETTER HEH GOAL FINAL FORM
            '\uFE94': '\u0647',  # ARABIC LETTER TEH MARBUTA FINAL FORM
            '\u0695': '\u0631',  # ARABIC LETTER REH WITH SMALL V BELOW
            '\u0673': '\u0627',  # ARABIC LETTER ALEF WITH WAVY HAMZA BELOW
            '\uFBAF': '\u06CC',  # ARABIC LETTER YEH BARREE FINAL FORM
            '\uFE86': '\u0648',  # ARABIC LETTER WAW WITH HAMZA ABOVE FINAL FORM
            '\uFB8A': '\u0698',  # ARABIC LETTER JEH ISOLATED FORM
            '\u0766': '\u0645',  # ARABIC LETTER MEEM WITH DOT BELOW
            '\uFEBE': '\u0636',  # ARABIC LETTER DAD FINAL FORM
            '\uFEA5': '\u062E',  # ARABIC LETTER KHAH ISOLATED FORM
            '\u0676': '\u0648',  # ARABIC LETTER HIGH HAMZA WAW
            '\uFED9': '\u06A9',  # ARABIC LETTER KAF ISOLATED FORM
            '\uFE87': '\u0627',  # ARABIC LETTER ALEF WITH HAMZA BELOW ISOLATED FORM
            '\uFEBA': '\u0635',  # ARABIC LETTER SAD FINAL FORM
            '\u06FF': '\u0647',  # ARABIC LETTER HEH WITH INVERTED V
            '\uFEC6': '\u0638',  # ARABIC LETTER ZAH FINAL FORM
            '\u0765': '\u0645',  # ARABIC LETTER MEEM WITH DOT ABOVE
            '\uFE93': '\u0647',  # ARABIC LETTER TEH MARBUTA ISOLATED FORM
            '\u06FB': '\u0636',  # ARABIC LETTER DAD WITH DOT BELOW
            '\u0694': '\u0631',  # ARABIC LETTER REH WITH DOT BELOW
            '\u06C7': '\u0648',  # ARABIC LETTER U
            '\u06FA': '\u0634',  # ARABIC LETTER SHEEN WITH DOT BELOW
            '\u06FE': '\u0645',  # ARABIC SIGN SINDHI POSTPOSITION MEN
            '\uFB7A': '\u0686',  # ARABIC LETTER TCHEH ISOLATED FORM
            '\uFECE': '\u063A',  # ARABIC LETTER GHAIN FINAL FORM
            '\u06B6': '\u0644',  # ARABIC LETTER LAM WITH DOT ABOVE
            '\uFBAE': '\u06CC',  # ARABIC LETTER YEH BARREE ISOLATED FORM
            '\u06BC': '\u0646',  # ARABIC LETTER NOON WITH RING
            '\uFBA5': '\u0647',  # ARABIC LETTER HEH WITH YEH ABOVE FINAL FORM
            '\u06CF': '\u0648',  # ARABIC LETTER WAW WITH DOT ABOVE
            '\uFE85': '\u0648',  # ARABIC LETTER WAW WITH HAMZA ABOVE ISOLATED FORM
            '\uFBA4': '\u0647',  # ARABIC LETTER HEH WITH YEH ABOVE ISOLATED FORM
            '\uFEC5': '\u0638',  # ARABIC LETTER ZAH ISOLATED FORM
            '\uFBAC': '\u0647',  # ARABIC LETTER HEH DOACHASHMEE INITIAL FORM
            '\uFE9B': '\u062B',  # ARABIC LETTER THEH INITIAL FORM
            '\u06CA': '\u0648',  # ARABIC LETTER WAW WITH TWO DOTS ABOVE
            '\u0622': '\u0627',  # ARABIC LETTER ALEF WITH MADDA ABOVE
        }

    def normalize(self, text: str) -> str:
        text = unicodedata.normalize('NFKC', text)
        temp = ''
        length = len(text)

        for i, c in enumerate(text):
            if c == '/' and 0 < i < length - 1 and text[i - 1].isnumeric() and text[i + 1].isnumeric():
                temp += '.'
                continue

            if c in self.valid_chars:
                temp += c
                continue

            if c in self.replace_map:
                temp += self.replace_map[c]
            else:
                temp += ' '

        # substitute multiple whitespace with single whitespace
        temp = re.sub(r'\s+', ' ', temp).strip()

        return temp
