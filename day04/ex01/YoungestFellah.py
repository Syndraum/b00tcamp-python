def youngestFellah(data, year):
    f = data.loc[(data['Year'] == year) & (data['Sex'] == 'F'), "Age"].min()
    m = data.loc[(data['Year'] == year) & (data['Sex'] == 'M'), "Age"].min()
    return {'f': f, 'm': m}


def proportionBySport(data, year, sport, gender):
    select = data.loc[
        (data['Year'] == year) &
        (data['Sex'] == gender), ["ID", "Sport"]]
    sport = select.loc[(select['Sport'] == sport), ["ID"]]
    return (sport['ID'].nunique() / select['ID'].nunique())


def howManyMedals(data, name):
    medal = {}
    select = data.loc[data["Name"] == name].groupby(['Year'])
    for index, value in select:
        medal[index] = {
            'G': len(value.loc[value['Medal'] == 'Gold'].index),
            'S': len(value.loc[value['Medal'] == 'Silver'].index),
            'B': len(value.loc[value['Medal'] == 'Bronze'].index)}
    return (medal)


def howManyMedalsByCountry(data, country):
    medal = {}
    select = data.loc[data["Team"] == country].groupby(['Year'])
    for index, value in select:
        medal[index] = {
            'G': value.loc[value['Medal'] == 'Gold']["Event"].nunique(),
            'S': value.loc[value['Medal'] == 'Silver']["Event"].nunique(),
            'B': value.loc[value['Medal'] == 'Bronze']["Event"].nunique()}
    return (medal)


class SpatioTemporalData:
    def __init__(self, data):
        self.data = data

    def when(self, location):
        lst = []
        select = self.data.loc[self.data["City"] == location].groupby(['Year'])
        for index, value in select:
            lst.append(index)
        return lst

    def where(self, date):
        return self.data.loc[self.data["Year"] == date].iloc[0]['City']
