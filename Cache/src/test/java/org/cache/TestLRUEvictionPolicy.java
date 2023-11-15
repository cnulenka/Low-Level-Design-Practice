package org.cache;

import org.cache.eviction.LRUEvictionPolicy;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class TestLRUEvictionPolicy {
    LRUEvictionPolicy<Integer> lruEvictionPolicy;

    @BeforeEach
    void setUp(){
        lruEvictionPolicy = new LRUEvictionPolicy<>();
    }

    @Test
    void testNullKeyEvict(){
        assertNull(lruEvictionPolicy.evict());
    }

    @Test
    void testKeyKeyAreEvictedInOrderOfAccess(){
        lruEvictionPolicy.keyAccessed(1);
        lruEvictionPolicy.keyAccessed(2);
        lruEvictionPolicy.keyAccessed(3);
        lruEvictionPolicy.keyAccessed(4);
        assertEquals(1, lruEvictionPolicy.evict());
        assertEquals(2, lruEvictionPolicy.evict());
        assertEquals(3, lruEvictionPolicy.evict());
        assertEquals(4, lruEvictionPolicy.evict());
    }

    @Test
    void testReaccesingKeyPreventsItFromEviction() {
        lruEvictionPolicy.keyAccessed(1);
        lruEvictionPolicy.keyAccessed(2);
        lruEvictionPolicy.keyAccessed(3);
        lruEvictionPolicy.keyAccessed(2);
        lruEvictionPolicy.keyAccessed(4);
        lruEvictionPolicy.keyAccessed(1);
        lruEvictionPolicy.keyAccessed(5);
        assertEquals(3, lruEvictionPolicy.evict());
        assertEquals(2, lruEvictionPolicy.evict());
        assertEquals(4, lruEvictionPolicy.evict());
        assertEquals(1, lruEvictionPolicy.evict());
        assertEquals(5, lruEvictionPolicy.evict());
    }
}
