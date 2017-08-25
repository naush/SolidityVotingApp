import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_item_has_name(self):
        items = [Item(name="foo", sell_in=10, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_item_quality_degrades_at_end_of_day(self):
        items = [Item("foo", sell_in=10, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].quality)

    def test_item_quality_degrades_twice_as_fast_after_sell_by_date(self):
        items = [Item("foo", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)

    def test_item_quality_is_never_negative(self):
        items = [Item("foo", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_aged_brie_quality_increases_the_older_it_gets(self):
        items = [Item("Aged Brie", sell_in=10, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(11, items[0].quality)

    def test_item_quality_never_over_50(self):
        items = [Item("Aged Brie", sell_in=10, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)

    def test_backstage_passes_increases_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(11, items[0].quality)

    def test_backstage_passes_increases_quality_by_2_when_10_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(12, items[0].quality)

    def test_backstage_passes_increases_quality_by_3_when_5_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(13, items[0].quality)

    def test_backstage_passes_quality_is_zero_after_the_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_conjured_item_degrades_twice_as_fast(self):
        items = [Item("Conjured mana cake", sell_in=10, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)

    def test_conjured_item_degrades_twice_as_fast_after_sell_in(self):
        items = [Item("Conjured mana cake", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(6, items[0].quality)

    def test_conjured_item_quality_is_never_negative(self):
        items = [Item("Conjured mana cake", sell_in=10, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_conjured_item_decreases_sell_in(self):
        items = [Item("Conjured mana cake", sell_in=10, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
