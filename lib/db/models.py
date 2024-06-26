from db.__init__ import CURSOR, CONN #import the __init__ to use the db
import pygame



class Band:
    #dict because I have a database which is the label.db
    #efficiency thing of the ORM
    #allows you to instantly look up an item in the database
    all = {}

    def __init__(self, name, id=None):
        self.id = id #unique identifier for the band
        self.name = name 
        
    def __repr__(self):
        return f"<Band {self.id} {self.name} >"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Band instances """
        sql = """
            CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY, 
            name TEXT)        
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Band instances """
        sql = """
            DROP TABLE IF EXISTS bands;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name value of the current Band instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO bands (name)
            VALUES (?)        
        """
        #Execute the SQL command to insert a new band
        CURSOR.execute(sql, (self.name,))
        #Commit the changes to the database
        CONN.commit()
        #update the bands ID with the primary keyu of teh newly inserted row
        self.id = CURSOR.lastrowid
        #Store the band instance in the dictionary
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """ Initialize a new Band instance and save the object to the database """
        band = cls(name)
        band.save()
        return band

    def update(self):
        """ Update the table row corresponding to the current Band instance """
        sql = """
            UPDATE bands
            SET name = ?,
            WHERE id = ?         
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """ Delete the table corresponding to the current Band instance,
        delete the dictionary entry, and reassign id attribute
        """
        sql = """
            DELETE FROM bands
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        #Delete teh band instance from the dict
        del type(self).all[self.id]
        #Reset the bands
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """ Return a Band object having to attribute values from the table row. """
        # Use primary key to check from instance
        band = cls.all.get(row[0])
        if band:
            band.name = row[1]
        else:
            band = cls(row[1])
            band.id = row[0]
            cls.all[band.id] = band
        return band

    @classmethod
    def get_all(cls):
        """ Return a list containing a Band object per row in the table. """
        sql = """
            SELECT *
            FROM bands
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """ Return a Band object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM bands
            WHERE id = ?   
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """ Return a Band object corresponding to first table row matching specified name. """
        sql = """
            SELECT *
            FROM bands
            WHERE name is ? 
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def members(self):
        """ Return list of members associated with current band. """
        sql = """ 
            SELECT * FROM members
            WHERE band_id = ? 
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        return [Member.instance_from_db(row) for row in rows]
   
    @classmethod
    def songs(self):
        """ Return list of songs associated with current band. """
        sql = """ 
            SELECT * FROM songs
            WHERE band_id = ? 
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        return [Song.instance_from_db(row) for row in rows]

class Member:
    all = {}

    def __init__(self, name, instrument, band_id, id=None):
        self.id = id
        self.name = name
        self.instrument = instrument
        self._band_id = band_id
        
    def __repr__(self):
        return (
            f"<Member {self.id}: {self.name}, {self.band_id}, " +
            f"Band ID: {self.band_id}>"
        )

    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
    
    @property 
    def instrument(self):
        return self._instrument
    
    @instrument.setter
    def instrument(self, instrument):
        if isinstance(instrument, str) and len(instrument):
            self._instrument = instrument
        else:
            raise ValueError(
                "instrument must be a non-empty string"
            )
        
    @property 
    def band_id(self):
        return self._band_id
    
    @band_id.setter
    def band_id(self, band_id):
        if type(band_id) is int and Band.find_by_id(band_id):
            self._band_id = band_id
        else:
            raise ValueError(
                "band_id must reference a band in the database."
            )
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Member instances """
        sql = """
            CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            instrument TEXT, 
            band_id INTEGER, 
            FOREIGN KEY (band_id) REFERENCES bands(id))     
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Member instances """
        sql = """
            DROP TABLE IF EXISTS members;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Instert a new row with the name, instrument and the band id values of the current Member object. 
        Update the object id attribute useing the primary key value of new row.
        Save the object in local dictionary using table row's PK as a dictionary key"""
        sql = """
            INSERT INTO members (name, instrument, band_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.instrument, self.band_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """ Update the table row corresponding to the current Member instance. """
        sql = """
            UPDATE members
            SET name = ?, instrument = ?, band_id = ?
            WHERE id = ?  
        """
        CURSOR.execute(sql, (self.name, self.instrument, self.band_id, self.id))
        CONN.commit()

    def delete(self):
        """ Delete the table row corresponding to the current Member instance, delete the dictionary
        entry, and reassign id attribute. """
    
        sql = """
            DELETE FROM members
            WHERE id = ?       
        """
    
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls, name, instrument, band_id):
        """ Initialize a new Member instance and save the object to the database. """
        if not Band.find_by_id(band_id):
            raise ValueError("band_id does not reference a band in the database")
        try:
            member = cls(name, instrument, band_id)
            member.save()
            return member
        except ValueError as e:
            print(f"error creating member: {e}")
            return None    
        
    @classmethod
    def instance_from_db(cls, row):
        """ Return a Member object haviong the attribute values from the table row. """
        
        # See if instance exists in the dict using primary key
        member = cls.all.get(row[0])
        if member:
            # Check if values match in case modification was made    
            member.name = row[1]
            member.instrument = row[2]
            member.band_id = row[3]
        else:
            # Create new instance if it doesn't exist in dictionary
            member = cls(row[1], row[2], row[3])
            member.id = row[0]
            cls.all[member.id] = member
        return member
    
    @classmethod
    def get_all(cls):
        """ Return a list containing one Member object per table row. """
        sql = """
            SELECT *
            FROM members
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """ Return Member object corresponding to the table row matching the specified primary key. """
        sql = """
            SELECT *
            FROM members
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod 
    def find_by_name(cls, name):
        """Return Member object corresponding to the first table row matching specified name"""
        sql = """
            SELECT *
            FROM members
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_instrument(cls, instrument):
        """Return the list of Member objects corresponding to the specified instrument."""
        sql = """
            SELECT *
            FROM members
            WHERE instrument = ?
        """
        rows = CURSOR.execute(sql, (instrument,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    

class Song:

    all = {}
    
    def __init__(self, name, path, band_id, id=None):
        self.id = id
        self.name = name
        self.path = path
        self.band_id = band_id

    def __repr__(self):
        return f"<Song {self.id} {self.name} {self.path} Band ID: {self.band_id}>" 
    
    ##may need to use: path TEXT UNIQUE,
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Song instances """
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY, 
            name TEXT,
            path TEXT, 
            band_id INTEGER,
            FOREIGN KEY (band_id) REFERENCES bands(id))        
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS songs;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create(cls, name, path, band_id):
        """ Initialize a new Song instance and save the object to the database. """
        if not Band.find_by_id(band_id):
            raise ValueError("band_id does not reference a band in the database")
        try:
            song = cls(name, path, band_id)
            song.save()
            return song
        except ValueError as e:
            print(f"error creating member: {e}")
            return None    
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM songs WHERE name = ?    
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        if row:
            return cls(row[1], row[2], row[3], row[0])
        return None
    
    @classmethod
    def find_by_id(cls, band_id):
        sql = """
            SELECT * FROM songs WHERE band_id = ?
        """
        rows = CURSOR.execute(sql, (band_id,)).fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return a Song object haviong the attribute values from the table row. """
        # See if instance exists in the dict using primary key       
        band = Band.find_by_id(int(row[3]))
        if not band:
            raise ValueError("band_id must reference a band")        
        song = cls.all.get(row[0])
        if song:
            # Check if values match in case modification was made    
            song.name = row[1]
            song.path = row[2]
            song.band_id = row[3]
        else:
            # Create new instance if it doesn't exist in dictionary
            song = cls(row[1], row[2], row[3])
            song.id = row[0]
            cls.all[song.id] = song
        return song

    @classmethod
    def get_all(cls):
        """ Return a list containing a Song object per row in the table. """
        sql = """
            SELECT *
            FROM songs
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def play(self):
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.path)) 
    
    def save(self):
        """ Instert a new row with the name, instrument and the band id values of the current Member object. 
        Update the object id attribute useing the primary key value of new row.
        Save the object in local dictionary using table row's PK as a dictionary key"""
        sql = """
            INSERT INTO songs (name, path, band_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.path, self.band_id))
        CONN.commit()

    @property 
    def band_id(self):
        return self._band_id
    
    @band_id.setter
    def band_id(self, band_id):
        if isinstance(band_id, int) and Band.find_by_id(band_id):
            self._band_id = band_id
        else:
            raise ValueError(
                "band_id must reference a band in the database."
            )