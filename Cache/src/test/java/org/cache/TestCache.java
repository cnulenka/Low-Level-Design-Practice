package org.cache;

import org.cache.eviction.LRUEvictionPolicy;
import org.cache.exceptions.KeyNotFoundException;
import org.cache.storage.HashMapStorage;
import org.cache.storage.Storage;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;

import static org.junit.jupiter.api.Assertions.*;

public class TestCache {
    Cache<Integer, Integer> cache;

    @BeforeEach
    void setUp(){
        LRUEvictionPolicy<Integer> lruEvictionPolicy = new LRUEvictionPolicy<>();
        Storage<Integer, Integer> storage = new HashMapStorage<>(3);
        cache = new Cache<>(lruEvictionPolicy, storage);
    }

    @Test
    void testPutAndGet() throws KeyNotFoundException {
        cache.put(1, 3);
        assertEquals(3, cache.get(1));
    }

    @Test
    void testKeyNotFound() {
        assertNull(cache.get(1));
    }

    @Test
    void testEviction() throws KeyNotFoundException {
        cache.put(1, 3);
        cache.put(2, 3);
        cache.put(3, 3);
        cache.put(4, 3);
        assertNull(cache.get(1));
    }

    @Test
    void testEviction2() throws KeyNotFoundException {
        cache.put(1, 3);
        cache.put(2, 3);
        cache.put(3, 3);
        cache.put(1, 3);
        cache.put(4, 3);
        assertNull(cache.get(2));
    }

}
