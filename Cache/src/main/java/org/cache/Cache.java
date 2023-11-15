package org.cache;

import org.cache.eviction.EvictionPolicy;
import org.cache.exceptions.KeyNotFoundException;
import org.cache.exceptions.StorageFullException;
import org.cache.storage.Storage;

public class Cache <Key, Value> {

    EvictionPolicy<Key> evictionPolicy;
    Storage<Key, Value> storage;

    public Cache(EvictionPolicy evictionPolicy, Storage storage){
        this.evictionPolicy = evictionPolicy;
        this.storage = storage;
    }

    public Value get(Key key) {
        try {
            Value value = storage.get(key);
            evictionPolicy.keyAccessed(key);
            return value;
        } catch (KeyNotFoundException e){
            System.out.println("Tried to access non-existing key.");
            return null;
        }
    }

    public void put (Key key, Value value) throws KeyNotFoundException {
        try {
            storage.put(key, value);
            evictionPolicy.keyAccessed(key);
        } catch (StorageFullException e){
            System.out.println("Got storage full. Will try to evict.");
            Key evictedKey = evictionPolicy.evict();
            if (evictedKey == null) { // Sanity check, good to have
                throw new RuntimeException("Unexpected State. Storage full and no key to evict.");
            }
            storage.remove(evictedKey);
            System.out.println("Creating space by evicting item..." + evictedKey);
            put(key, value);
        }
    }
}
