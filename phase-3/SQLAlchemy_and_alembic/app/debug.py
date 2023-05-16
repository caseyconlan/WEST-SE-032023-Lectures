
# 3.✅ CRUD practice
# To run the file run `python3 console.py` in the app directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Pet)

if __name__ == '__main__':
    # 3.1 ✅ Uncomment bellow to create the engine
    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)
    # 3.2 ✅ Uncomment bellow to create sessions and bind o the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3.3 ✅  -- Creating records
    # Create a pet and save it to the data base with session.add and session.commit
    # rose = Pet(name="Rose", species="dog", breed="poodle", temperament="happy")
    # # Create multiple pets and bulk save them with  session.bulk_save_objects and session.commit
    # golden_retriever_names = ["Bob", "Jane", "Mary", "Bill"]
    # golden_retrievers = [Pet(name=name, species="dog", breed="golden retriever", temperament="sad")
    #                      for name in golden_retriever_names]

    # # session.bulk_save_objects(golden_retrievers)
    # # session.commit()

    pets = [pet for pet in session.query(Pet)]

    pet_names = [name for name in session.query(Pet.name)]

    sad_pets = [pet for pet in session.query(
        Pet).filter(Pet.temperament.like('%sad%'))]

    first_pet = session.query(Pet).first()

    # session.delete(first_pet)
    # session.commit()

    # session.query(Pet).delete()
    # session.commit()

    # first_pet.name = "Original Rose"

    # session.query(Pet).update({Pet.temperament: "Excited"})

    # session.commit()

    # session.add(rose)
    # Note: bulk save will not contain the id

    # verify by checking the db
    # 3.4 ✅ Read
    # Get all with session.query
    # Print the pets

    # Get all of the pet names and print them with session.query

    # Get all the pet names and print them in order with session.query and order_by

    # Get the first pet with session.query and first

    # Filter pet by temperament with session.query and filter

    # 3.5 ✅ Update
    # Update the pets name and print the updated pet info

    # Update all the pets temperament to 'cool' and print the pets

    # 3.6 ✅  Delete
    # Delete one item by querying the first pet, deleting it and committing it

    # delete all the pets with session.query and .delete

    # optional Break point for debugging and testing
    import ipdb
    ipdb.set_trace()
