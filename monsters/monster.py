class Monster:
  def __init__(self, name, hp, level):
    self.__name = name
    self.__hp = hp
    self.__level = level

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, name):
    self.__name = name

  @property
  def hp(self):
    return self.__hp

  @hp.setter
  def hp(self, hp):
    self.__hp = hp

  @property
  def level(self):
    return self.__level

  @level.setter
  def level(self, level):
    self.__level = level

  def __hash__(self):
    return hash(self.__name) ^ hash(self.__level) ^ hash(self.__hp)

  def __eq__(self, other):
    return isinstance(other,
                      self.__class__) and self.__name == other.__name and self.__level == other.__level and self.__hp == other.__hp

  def __ne__(self, other):
    return (not self.__eq__(other))

  def __str__(self):
    return 'Monster: {name: %s, level: %s, hp: %i}' % (self.__name, self.__level, self.__hp)

  __repr__ = __str__
