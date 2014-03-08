from anki import Collection as coll

import os

benchDir = os.path.dirname(__file__)
runDir = os.getcwd()

def test_run():
    col = coll(os.path.join(benchDir, "collection.anki2"))
    for i in range(50):
        col.models._updateRequired(col.models.current())
    col.db.close()
    os.chdir(runDir)

if __name__ == "__main__":
    test_run()
