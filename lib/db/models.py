from db.__init__ import CURSOR, CONN


class Band:

    all = {}

    def __init__(self, name, time, id=None):
        self.id = id
        self.name = name
        self.time = time

    def __repr__(self):
        return f"<Band {self.id} {self.name}, {self.time}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-emptry string"
            )
        
    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, time):
        if isinstance(time, int) and 6 <= time <= 10:
            self._time = time
        else: 
            raise ValueError(
                "Time must be a non-empty number between 7 and 10"
            )
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Band instances """
        sql = """
            CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            time INTEGER)        
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the tale that persists Band instances """
        sql = """
            DROP TABLE IF EXISTS bands;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and time values of the current Band instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO bands (name, time)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.time))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, time):
        """ Initialize a new Band instance and save the object to the database """
        band = cls(name, time)
        band.save()
        return band

    def update(self):
        """ Update the table row corresponding to the current Band instance """
        sql = """
            UPDATE bands
            SET name = ?, time = ?
            WHERE id = ?         
        """
        CURSOR.execute(sql, (self.name, self.time, self.id))
        CONN.commit()
    
    def delete(self):
        """ Delete teh table corresponding to the current Band instance,
        delete the dictionary entry, and reassign id attribute
        """
        sql = """
            DELETE FROM bands
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """ Return a Band object having to attribute values from the table row. """
        #use primary key to check from instance
        band = cls.all.get(row[0])
        if band:
            band.name = row[1]
            band.time = row[2]
        else:
            band = cls(row[1], row[2])
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

        row = CURSOR.execute(sql, (name, )).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def members(self):
        """ Return list of members associated woth current band. """
       
        sql = """ 
            SELECT * FROM members
            WHERE band_id = ? 
        """
        CURSOR.execute(sql, (self.id,))

        rows = CURSOR.fetchall()
        return [
            Member.instance_from_db(row) for row in rows
        ]
####################################
    @classmethod
    def find_by_time(cls, time):
        """ Return a Band object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM bands
            WHERE time= ?   
        """

        row = CURSOR.execute(sql, (time,)).fetchone()
        return cls.instance_from_db(row) if row else None
##################################################


class Member:
    all = {}

    def __init__(self, name, instrument, band_id, id=None):
        self.id = id
        self.name = name
        self.instrument = instrument
        self.band_id = band_id
        
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
        member = cls(name, instrument, band_id)
        member.save()
        return member
    
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
            FROM employees
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

            
    