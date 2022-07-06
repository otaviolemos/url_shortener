from abc import ABC, abstractmethod

class URLRepo(ABC):
  @abstractmethod
  def add(self, id, longUrl, hash):
    pass

  @abstractmethod
  def get(self, longUrl):
    pass