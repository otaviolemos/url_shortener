from abc import ABC, abstractmethod

class URLRepo(ABC):
  @abstractmethod
  def add(self, id, longUrl, hash):
    pass

  @abstractmethod
  def list(self):
    pass

  @abstractmethod
  def findByLongUrl(self, longUrl):
    pass