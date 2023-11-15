package org.cache.storage;

import org.cache.exceptions.KeyNotFoundException;
import org.cache.exceptions.StorageFullException;

public interface Storage<Key, Value> {
    public Value get(Key key) throws KeyNotFoundException;
    public void remove(Key key) throws KeyNotFoundException;
    public void put(Key key, Value value) throws StorageFullException;
}
