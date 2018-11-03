from re import findall, match

class Helpers:
    token_regex = "\[([^\[\]]+)\]"
    intra_token_regex = "([\d]+):[\w]+"

    def parse_post(self, input):
        hits = findall(self.token_regex, input)

        entries = []
        for hit in hits:
            entry = {}

            id_hit = match(self.intra_token_regex, hit)
            if (id_hit):
                entry['id'] = int(id_hit.group(1))
            else:
                splitIndex = hit.find(" ")
                if splitIndex != -1:
                    entry['firstName'] = hit[:splitIndex]
                    entry['lastName'] = hit[splitIndex+1:]
                else: 
                    continue

            entries.append(entry)

        return entries

