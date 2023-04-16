from lib.db import db
class TestMigration:
  def migrate_sql():
    data = """
      ALTER TABLE public.users ADD COLUMN bio text;
    """
    return data
  def rollback_sql():
    data = """
    ALTER TABLE public.users DROP COLUMN;
    """
    return data
  def migrate():
    db.query_commit(TestMigration.migrate_sql(),{
    })
  def rollback():
    db.query_commit(TestMigration.rollback_sql(),{
    })
migration = TestMigration  