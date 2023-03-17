import hashlib


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        sha256 = hashlib.sha256()
        sha256.update(str(key).encode())
        return int.from_bytes(sha256.digest(), byteorder="big") % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(str(key))

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError(str(key))


names = [
  "Astronomy",
  "Biology",
  "Chemistry",
  "DNA",
  "Ecology",
  "Fossils",
  "Genetics",
  "Hydrology",
  "Immunology",
  "Joule",
  "Kinetics",
  "Lithium",
  "Electromagnetism",
  "Neuroscience",
  "Organic Chemistry",
  "Physics",
  "Quantum Mechanics",
  "Relativity",
  "Solar Energy",
  "Thermodynamics",
  "Ultraviolet",
  "Virus",
  "Water Cycle",
  "X-rays",
  "Yeast",
  "Zoology",
  "Acid Rain",
  "Botany",
  "Cell Theory",
  "Dendrochronology",
  "Electromagnetism",
  "Forensic Science",
  "Geology",
  "Hypothesis",
  "Infrared",
  "Jupiter",
  "Kepler's Laws",
  "Laser",
  "Meteorology",
  "Nuclear Energy",
  "Oxygen",
  "Photosynthesis",
  "Quantum Computing",
  "Radioactivity",
  "Satellite",
  "Theory of Evolution",
  "Ultraviolet Radiation",
  "Vaccination",
  "Wave"
]



definitions = [
    "The study of celestial objects, such as stars, planets, and galaxies",
    "The study of living organisms and their interactions with each other and the environment",
    "The study of the composition, properties, and behavior of matter",
    "A self-replicating material that carries genetic information",
    "The study of the relationships between living organisms and their environment",
    "The remains or traces of organisms from a previous geological age",
    "The study of heredity and the variation of inherited characteristics",
    "The study of water in the Earth's system",
    "The study of the immune system and its responses to pathogens",
    "A unit of energy used in physics, named after James Prescott Joule",
    "The study of the rates of chemical reactions",
    "A soft, silvery-white metal with atomic number 3",
    "The study of electric and magnetic fields",
    "The study of the nervous system and the brain",
    "The study of compounds that contain carbon",
    "The study of matter, energy, and the interactions between them",
    "The branch of physics that deals with the behavior of matter and energy on a very small scale",
    "The branch of physics that deals with the relationship between space and time",
    "The study of using energy from the sun to produce electricity",
    "The study of heat and its relationship to other forms of energy",
    "A type of electromagnetic radiation that is just beyond the violet end of the visible spectrum",
    "An infectious agent that replicates inside the cells of living hosts",
    "The continuous movement of water on, above, and below the surface of the Earth",
    "A type of electromagnetic radiation with a shorter wavelength than visible light",
    "A single-celled organism used in scientific research and baking",
    "The study of animals and their behavior, physiology, and evolution",
    "Rainfall that is more acidic than normal",
    "The study of plants and their anatomy, growth, and classification",
    "The theory that all living things are composed of cells and that cells are the basic units of life",
    "The study of tree rings to determine past climate and environmental conditions",
    "The study of the relationships between electric currents and magnetic fields",
    "The use of scientific methods to solve crimes and legal issues",
    "The study of the Earth's physical structure and substance",
    "A proposed explanation for an observation or phenomenon that can be tested",
    "A type of electromagnetic radiation with a longer wavelength than visible light",
    "The largest planet in the solar system",
    "Three laws that describe the motion of planets around the sun, proposed by Johannes Kepler",
    "A device that emits a narrow, intense beam of light",
    "The study of the Earth's atmosphere and its weather patterns",
    "The energy released during a nuclear reaction, such as fusion or fission",
    "A colorless, odorless gas that is essential for life",
    "The process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll",
    "The study of the development of computer technology based on quantum theory",
    "The emission of ionizing radiation or particles caused by the spontaneous disintegration of atomic nuclei",
    "An object in space that orbits around a planet or a star",
    "The scientific explanation for the diversity of life on Earth, proposed by Charles Darwin",
    "A type of electromagnetic radiation with a shorter wavelength than visible light",
    "The administration of a vaccine to stimulate the immune system and provide protection against a disease",
    "A disturbance that travels through space and time",
]

print(len(names))
print(len(definitions))


hash_table = HashTable(len(names))
for i, name in enumerate(names):
    hash_table.insert(name, definitions[i])


print(hash_table.table)
