#kelas ini menyimpan part dan icon yang di tampilkan
class Parts:
    def __init__(self) -> None:
        self.mode_bg = {
            'n':'#6f03fc',
            'i':'#000000',
            'v':'#888888',
            '\x16':'#888888',
            'V':'#888888',
            'R':'#000000',
            't':'#888888',
            'c':'#888888',
        }
        self.icon_file = '󱔘'
        self.icon_branch = ''
        self.file_name = '%t%m'
        self.row_col= '%l:%c'
        self.section_1 = '#6f03fc'
        self.section_2 = '#6f03fc'
        self.section_3= '#6f03fc'
        self.font_weight = 'NONE'
        self.make_coloum = '%='
        self.border_right = ''
        self.border_left = ''
        self.separator = '•'
        self.icon_mode ='󰭕'
        self.default_border_bg ='#FF000000'

