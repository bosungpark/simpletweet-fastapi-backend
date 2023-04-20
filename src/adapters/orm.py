in_memory_orm = ...

def in_memory_db(url):
    engine = create_engine(url, connect_args={"check_same_thread": False}, future=True)
    in_memory_orm.metadata.create_all(engine)
    return engine