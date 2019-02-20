class ResultOutputer(object):
    def add_data(self, all_data):
        with open('results.html', 'w', encoding='utf8') as fout:
            fout.write('<table>')

            for data in all_data:
                fout.write('<tr>')
                fout.write('<td>')
                fout.write(data['title'])
                fout.write('</td>')
                fout.write('<td>')
                fout.write(data['intro'])
                fout.write('</td>')
                fout.write('</tr>')
            fout.write('</table>')