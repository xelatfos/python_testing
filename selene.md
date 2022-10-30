By default element finders (browser.element, browser.all) accept css selectors as strings, but you can use any custom selector from the by module.

There are such by selectors for searching by xpath, text, part of text or attribute in Selene:

by.css(selector)

e.g. s(by.css('.edit').click()

by.xpath(selector)

e.g. s(by.xpath(".//*[@class='price']")).click()

by.name(name)

e.g. s(by.name('nav')).click()

by.link_text(text)

e.g. s(by.link_text('Active')).click()

by.partial_link_text(text)

e.g. s(by.partial_link_text('Act')).click()

by.text(element_text)

e.g. s(by.text('Product')).click()

by.partial_text(element_text) | with_text (element_text)

e.g. s(by.text('Prod')).click()

by.be_first_child()

e.g. s('#element').element(by.be_first_child).click()

by.be_following_sibling()

e.g. s('#element').element(by.be_following_sibling).click()

by.be_parent()

e.g. s('#element').element(by.be_parent).click()