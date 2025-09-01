"""11DGT Python games compendium assessment. Contains text based games which includes speed typing, wordle and paper scissors rock. 
Each game has a leaderboard system that can be seen."""
import time
import random
action = 0   #Placeholder variables and word lists that are used later in the code
fastest_time_record = (999999, "No one")
highest_wordle_streak = (0, "No one")
highest_paper_scissors_rock_streak = (0, "No one")
typing_words_list = [
    'a', 'about', 'all', 'also', 'and', 'as', 'at', 'be', 'because', 'but',
    'by', 'can', 'come', 'could', 'day', 'do', 'even', 'find', 'first', 'for',
    'from', 'get', 'give', 'go', 'have', 'he', 'her', 'here', 'him', 'his',
    'how', 'I', 'if', 'in', 'into', 'it', 'its', 'just', 'know', 'like',
    'look', 'make', 'man', 'many', 'me', 'more', 'my', 'new', 'no', 'not',
    'now', 'of', 'on', 'one', 'only', 'or', 'other', 'our', 'out', 'people',
    'say', 'see', 'she', 'so', 'some', 'take', 'tell', 'than', 'that', 'the',
    'their', 'them', 'then', 'there', 'these', 'they', 'thing', 'think', 'this', 'those',
    'time', 'to', 'two', 'up', 'use', 'very', 'want', 'way', 'we', 'well',
    'what', 'when', 'which', 'who', 'will', 'with', 'would', 'year', 'you', 'your',
    'able', 'above', 'across', 'act', 'add', 'afraid', 'after', 'again', 'against', 'age',
    'ago', 'agree', 'air', 'all', 'allow', 'almost', 'alone', 'along', 'already', 'also',
    'although', 'always', 'am', 'among', 'an', 'and', 'anger', 'animal', 'another', 'answer',
    'any', 'anyone', 'anything', 'appear', 'apply', 'approach', 'are', 'area', 'argue', 'arm',
    'around', 'arrive', 'art', 'as', 'ask', 'at', 'attack', 'aunt', 'author', 'away',
    'baby', 'back', 'bad', 'bag', 'ball', 'bank', 'bar', 'base', 'be', 'bear',
    'beat', 'beautiful', 'because', 'become', 'bed', 'before', 'begin', 'behavior', 'behind', 'believe',
    'below', 'beneath', 'beside', 'best', 'better', 'between', 'beyond', 'big', 'bill', 'bird',
    'birth', 'bit', 'black', 'blood', 'blue', 'board', 'boat', 'body', 'book', 'born',
    'both', 'bother', 'bottle', 'bottom', 'box', 'boy', 'branch', 'brave', 'bread', 'break',
    'breakfast', 'breathe', 'bridge', 'brief', 'bright', 'bring', 'broad', 'brother', 'brown', 'build',
    'burn', 'bus', 'business', 'busy', 'but', 'buy', 'by', 'cake', 'call', 'can',
    'candle', 'cap', 'car', 'card', 'care', 'carry', 'case', 'cat', 'catch', 'cause',
    'celebrate', 'center', 'central', 'century', 'certain', 'chair', 'challenge', 'chance', 'change', 'character',
    'charge', 'chart', 'chase', 'cheap', 'check', 'cheese', 'chicken', 'child', 'choice', 'choose',
    'church', 'circle', 'city', 'claim', 'class', 'clean', 'clear', 'climb', 'clock', 'close',
    'clothes', 'cloud', 'club', 'coat', 'coffee', 'cold', 'collect', 'college', 'color', 'come',
    'common', 'company', 'compare', 'complain', 'complete', 'computer', 'concern', 'condition', 'consider', 'continue',
    'control', 'cook', 'cool', 'copy', 'corner', 'correct', 'cost', 'could', 'count', 'country',
    'course', 'cover', 'cow', 'create', 'crime', 'cross', 'crowd', 'cry', 'cup', 'current',
    'customer', 'cut', 'dad', 'dance', 'danger', 'dark', 'daughter', 'day', 'dead', 'deal',
    'dear', 'death', 'decide', 'deep', 'degree', 'depend', 'describe', 'design', 'destroy', 'develop',
    'die', 'different', 'difficult', 'dinner', 'direction', 'discover', 'discuss', 'disease', 'do', 'doctor',
    'dog', 'door', 'double', 'doubt', 'down', 'draw', 'dream', 'dress', 'drink', 'drive',
    'drop', 'drug', 'dry', 'during', 'dust', 'duty', 'each', 'ear', 'early', 'earn',
    'earth', 'easy', 'eat', 'economy', 'edge', 'education', 'effect', 'effort', 'egg', 'eight',
    'either', 'elect', 'electric', 'eleven', 'else', 'employee', 'empty', 'end', 'enemy', 'energy',
    'engine', 'enough', 'enter', 'environment', 'equal', 'especially', 'establish', 'even', 'evening', 'event',
    'ever', 'every', 'everyone', 'everything', 'evidence', 'exact', 'example', 'except', 'excite', 'exercise',
    'exist', 'expect', 'experience', 'expert', 'explain', 'express', 'extra', 'eye', 'face', 'fact',
    'fail', 'fall', 'family', 'famous', 'far', 'farm', 'fast', 'fat', 'father', 'fault',
    'fear', 'feed', 'feel', 'female', 'few', 'field', 'fight', 'figure', 'fill', 'film',
    'final', 'find', 'fine', 'finger', 'finish', 'fire', 'first', 'fish', 'five', 'fix',
    'flat', 'floor', 'flow', 'flower', 'fly', 'focus', 'follow', 'food', 'foot', 'for',
    'force', 'foreign', 'forest', 'forget', 'form', 'forward', 'four', 'free', 'fresh', 'friend',
    'from', 'front', 'fruit', 'full', 'fun', 'future', 'game', 'garden', 'gas', 'gather',
    'general', 'get', 'gift', 'girl', 'give', 'glad', 'glass', 'go', 'goal', 'god',
    'gold', 'good', 'government', 'grade', 'grand', 'grass', 'gray', 'great', 'green', 'ground',
    'group', 'grow', 'guess', 'guide', 'gun', 'guy', 'hair', 'half', 'hall', 'hand',
    'handle', 'hang', 'happen', 'happy', 'hard', 'has', 'hat', 'have', 'he', 'head',
    'health', 'hear', 'heart', 'heat', 'heavy', 'hello', 'help', 'her', 'here', 'herself',
    'high', 'hill', 'him', 'himself', 'his', 'history', 'hit', 'hold', 'hole', 'holiday',
    'home', 'hope', 'horse', 'hospital', 'hot', 'hotel', 'hour', 'house', 'how', 'however',
    'huge', 'human', 'hundred', 'hungry', 'hunt', 'hurry', 'hurt', 'husband', 'I', 'ice',
    'idea', 'if', 'imagine', 'important', 'improve', 'in', 'include', 'increase', 'indeed', 'indicate',
    'industry', 'inform', 'inside', 'instead', 'interest', 'international', 'into', 'introduce', 'invest', 'involve',
    'iron', 'is', 'island', 'issue', 'it', 'its', 'itself', 'job', 'join', 'joke',
    'judge', 'jump', 'junior', 'just', 'keep', 'key', 'kick', 'kid', 'kill', 'kind',
    'king', 'kiss', 'kitchen', 'knee', 'knife', 'know', 'knowledge', 'lady', 'lake', 'land',
    'language', 'large', 'last', 'late', 'laugh', 'law', 'lawyer', 'lay', 'lead', 'learn',
    'least', 'leave', 'left', 'leg', 'legal', 'less', 'let', 'letter', 'level', 'lie',
    'life', 'lift', 'light', 'like', 'likely', 'limit', 'line', 'link', 'lip', 'list',
    'listen', 'little', 'live', 'load', 'local', 'lock', 'long', 'look', 'lose', 'lot',
    'loud', 'love', 'low', 'luck', 'lunch', 'machine', 'magazine', 'main', 'maintain', 'major',
    'make', 'male', 'man', 'manage', 'many', 'map', 'mark', 'market', 'marry', 'master',
    'match', 'material', 'matter', 'may', 'maybe', 'me', 'meal', 'mean', 'measure', 'meat',
    'media', 'medical', 'meet', 'member', 'memory', 'mention', 'menu', 'mere', 'message', 'metal',
    'method', 'middle', 'might', 'mile', 'military', 'milk', 'million', 'mind', 'mine', 'minister',
    'minor', 'minute', 'miss', 'mistake', 'mix', 'model', 'modern', 'moment', 'money', 'month',
    'mood', 'more', 'morning', 'most', 'mother', 'motor', 'mountain', 'mouse', 'mouth', 'move',
    'movie', 'Mr', 'Mrs', 'much', 'music', 'must', 'my', 'myself', 'name', 'narrow',
    'nation', 'natural', 'nature', 'near', 'necessary', 'neck', 'need', 'negative', 'neighbor', 'neither',
    'nerve', 'never', 'new', 'news', 'next', 'nice', 'night', 'nine', 'no', 'nobody',
    'noise', 'none', 'nor', 'normal', 'north', 'nose', 'not', 'note', 'nothing', 'notice',
    'now', 'number', 'nurse', 'object', 'observe', 'obtain', 'obvious', 'occur', 'ocean', 'of',
    'off', 'offer', 'office', 'officer', 'official', 'often', 'oh', 'oil', 'ok', 'old',
    'on', 'once', 'one', 'only', 'onto', 'open', 'operate', 'opinion', 'opportunity', 'opposite',
    'or', 'orange', 'order', 'organize', 'other', 'otherwise', 'ought', 'our', 'ourselves', 'out',
    'outside', 'over', 'own', 'owner', 'page', 'pain', 'paint', 'pair', 'paper', 'parent',
    'park', 'part', 'particular', 'partner', 'party', 'pass', 'past', 'path', 'patient', 'pattern',
    'pay', 'peace', 'pen', 'pencil', 'people', 'per', 'percent', 'perfect', 'perform', 'perhaps',
    'period', 'person', 'personal', 'pet', 'phone', 'photo', 'physical', 'pick', 'picture', 'piece',
    'pig', 'pilot', 'pink', 'pipe', 'place', 'plan', 'plane', 'plant', 'plastic', 'plate',
    'play', 'player', 'please', 'pleasure', 'plenty', 'plus', 'pocket', 'poem', 'point', 'police',
    'policy', 'political', 'pool', 'poor', 'popular', 'population', 'position', 'positive', 'possible', 'post',
    'pot', 'potato', 'pound', 'power', 'practice', 'prepare', 'present', 'president', 'press', 'pressure',
    'pretty', 'prevent', 'previous', 'price', 'pride', 'priest', 'print', 'prior', 'private', 'prize',
    'probably', 'problem', 'process', 'produce', 'product', 'profession', 'professor', 'profile', 'profit', 'program',
    'progress', 'project', 'promise', 'promote', 'proper', 'property', 'protect', 'prove', 'provide', 'public',
    'pull', 'punish', 'purchase', 'purple', 'purpose', 'push', 'put', 'quality', 'quantity', 'quarter',
    'queen', 'question', 'quick', 'quiet', 'quit', 'quite', 'quote', 'race', 'radio', 'rain',
    'raise', 'range', 'rate', 'rather', 'reach', 'read', 'ready', 'real', 'reality', 'realize',
    'really', 'reason', 'receive', 'recent', 'recognize', 'record', 'red', 'reduce', 'refer', 'reflect',
    'refuse', 'regard', 'region', 'regular', 'relate', 'relax', 'release', 'religion', 'remain', 'remember',
    'remove', 'rent', 'repair', 'repeat', 'replace', 'reply', 'report', 'represent', 'require', 'research',
    'respect', 'respond', 'rest', 'restaurant', 'result', 'return', 'reveal', 'review', 'rich', 'ride',
    'right', 'ring', 'rise', 'risk', 'river', 'road', 'rock', 'role', 'roll', 'roof',
    'room', 'root', 'rope', 'rose', 'rough', 'round', 'route', 'routine', 'row', 'royal',
    'rub', 'rude', 'rule', 'run', 'rush', 'sad', 'safe', 'sail', 'sale', 'salt',
    'same', 'sample', 'sand', 'satellite', 'satisfy', 'save', 'say', 'scale', 'scare', 'scene',
    'school', 'science', 'score', 'scream', 'screen', 'sea', 'search', 'season', 'seat', 'second',
    'secret', 'section', 'see', 'seed', 'seek', 'seem', 'seize', 'sell', 'send', 'sense',
    'sentence', 'separate', 'series', 'serious', 'serve', 'service', 'set', 'settle', 'seven', 'several',
    'sex', 'shade', 'shadow', 'shake', 'shall', 'shape', 'share', 'sharp', 'she', 'sheet',
    'shelf', 'shell', 'shine', 'ship', 'shirt', 'shock', 'shoe', 'shoot', 'shop', 'short',
    'should', 'shoulder', 'shout', 'show', 'shut', 'sick', 'side', 'sight', 'sign', 'signal',
    'silence', 'silver', 'similar', 'simple', 'since', 'sing', 'single', 'sir', 'sister', 'sit',
    'site', 'situation', 'six', 'size', 'skill', 'skin', 'skirt', 'sky', 'sleep', 'slice',
    'slide', 'slight', 'slip', 'slow', 'small', 'smell', 'smile', 'smoke', 'snow', 'so',
    'soap', 'social', 'society', 'soft', 'soil', 'soldier', 'solid', 'solution', 'solve', 'some',
    'somebody', 'someone', 'something', 'sometimes', 'son', 'song', 'soon', 'sorry', 'sort', 'soul',
    'sound', 'soup', 'south', 'space', 'speak', 'special', 'specific', 'speech', 'speed', 'spell',
    'spend', 'spirit', 'spite', 'split', 'sport', 'spot', 'spread', 'spring', 'square', 'stable',
    'staff', 'stage', 'stair', 'stand', 'standard', 'star', 'start', 'state', 'station', 'stay',
    'steal', 'steam', 'steel', 'step', 'stick', 'still', 'stock', 'stomach', 'stone', 'stop',
    'store', 'storm', 'story', 'straight', 'strange', 'street', 'strength', 'stress', 'stretch', 'strike',
    'string', 'strip', 'stroke', 'strong', 'structure', 'struggle', 'student', 'study', 'stuff', 'stupid',
    'style', 'subject', 'submit', 'substance', 'succeed', 'success', 'such', 'sudden', 'suffer', 'sugar',
    'suggest', 'suit', 'summer', 'sun', 'super', 'supply', 'support', 'suppose', 'sure', 'surface',
    'surprise', 'surround', 'survive', 'suspect', 'swallow', 'swear', 'sweet', 'swim', 'swing', 'switch',
    'symbol', 'system', 'table', 'take', 'talk', 'tall', 'tank', 'tape', 'target', 'task',
    'taste', 'tax', 'tea', 'teach', 'teacher', 'team', 'tear', 'technology', 'telephone', 'television',
    'tell', 'temperature', 'ten', 'tend', 'term', 'test', 'than', 'thank', 'that', 'the',
    'their', 'them', 'themselves', 'then', 'theory', 'there', 'these', 'they', 'thick', 'thin',
    'thing', 'think', 'third', 'this', 'those', 'though', 'thought', 'thousand', 'threat', 'three',
    'throat', 'through', 'throw', 'thus', 'ticket', 'tie', 'tight', 'time', 'tiny', 'tip',
    'tire', 'title', 'to', 'today', 'toe', 'together', 'tomorrow', 'tone', 'tongue', 'tonight',
    'too', 'tool', 'tooth', 'top', 'total', 'touch', 'tough', 'tour', 'toward', 'tower',
    'town', 'toy', 'track', 'trade', 'tradition', 'traffic', 'train', 'transfer', 'transport', 'travel',
    'treat', 'tree', 'trend', 'trial', 'tribe', 'trick', 'trip', 'trouble', 'truck', 'true',
    'trust', 'truth', 'try', 'tube', 'turn', 'twelve', 'twenty', 'twice', 'two', 'type',
    'typical', 'ugly', 'uncle', 'under', 'understand', 'uniform', 'union', 'unique', 'unit', 'unite',
    'universe', 'university', 'unless', 'until', 'up', 'upon', 'upper', 'urban', 'us', 'use',
    'useful', 'user', 'usual', 'usually', 'vacation', 'valley', 'valuable', 'value', 'variety', 'various',
    'vary', 'vast', 'vegetable', 'vehicle', 'version', 'very', 'victim', 'victory', 'video', 'view',
    'village', 'violate', 'violence', 'virtual', 'virus', 'visit', 'visitor', 'voice', 'volume', 'vote',
    'wage', 'wait', 'wake', 'walk', 'wall', 'want', 'war', 'warm', 'warn', 'wash',
    'watch', 'water', 'wave', 'way', 'we', 'weak', 'wealth', 'weapon', 'wear', 'weather',
    'web', 'website', 'wedding', 'week', 'weekend', 'weigh', 'weight', 'welcome', 'well', 'west',
    'western', 'what', 'whatever', 'wheel', 'when', 'where', 'whether', 'which', 'while', 'white',
    'who', 'whole', 'whom', 'whose', 'why', 'wide', 'wife', 'wild', 'will', 'win',
    'wind', 'window', 'wine', 'wing', 'winner', 'winter', 'wipe', 'wire', 'wisdom', 'wise',
    'wish', 'with', 'within', 'without', 'witness', 'woman', 'wonder', 'wood', 'word', 'work',
    'worker', 'world', 'worry', 'worth', 'would', 'wound', 'wrap', 'write', 'writer', 'wrong',
    'yard', 'yeah', 'year', 'yellow', 'yes', 'yesterday', 'yet', 'yield', 'you', 'young',
    'your', 'yourself', 'youth', 'zone'
]
wordle_words_list = [
    'about', 'above', 'abuse', 'actor', 'acute', 'admit', 'adopt', 'adult', 'after', 'again',
    'agent', 'agree', 'ahead', 'alarm', 'album', 'alert', 'alike', 'alive', 'allow', 'alone',
    'along', 'alter', 'among', 'anger', 'angle', 'angry', 'apart', 'apple', 'apply', 'arena',
    'argue', 'arise', 'array', 'aside', 'asset', 'audio', 'audit', 'avoid', 'award', 'aware',
    'badly', 'baker', 'bases', 'basic', 'basis', 'beach', 'began', 'begin', 'begun', 'being',
    'below', 'bench', 'billy', 'birth', 'black', 'blame', 'blank', 'blast', 'blend', 'blind',
    'blink', 'block', 'blood', 'bloom', 'board', 'boost', 'booth', 'bound', 'brain', 'brand',
    'brave', 'bread', 'break', 'breed', 'brief', 'bring', 'broad', 'broke', 'brown', 'build',
    'built', 'bunch', 'burst', 'buyer', 'cable', 'calif', 'carry', 'catch', 'cause', 'chain',
    'chair', 'chart', 'chase', 'cheap', 'check', 'chest', 'chief', 'child', 'china', 'chose',
    'civil', 'claim', 'class', 'clean', 'clear', 'click', 'clock', 'close', 'coach', 'coast',
    'could', 'count', 'court', 'cover', 'craft', 'crash', 'cream', 'crime', 'cross', 'crowd',
    'crown', 'curve', 'cycle', 'daily', 'dance', 'dated', 'dealt', 'death', 'debut', 'delay',
    'depth', 'doing', 'doubt', 'dozen', 'draft', 'drama', 'drawn', 'dream', 'dress', 'drill',
    'drink', 'drive', 'drove', 'dying', 'eager', 'early', 'earth', 'eight', 'elite', 'empty',
    'enemy', 'enjoy', 'enter', 'entry', 'equal', 'error', 'essay', 'event', 'every', 'exact',
    'excel', 'exist', 'extra', 'faith', 'false', 'fault', 'favor', 'fence', 'fever', 'fewer',
    'fiber', 'field', 'fifth', 'fifty', 'fight', 'final', 'first', 'fixed', 'flame', 'flash',
    'fleet', 'floor', 'fluid', 'focus', 'force', 'forth', 'forty', 'forum', 'found', 'frame',
    'frank', 'fraud', 'fresh', 'front', 'fruit', 'fully', 'funny', 'giant', 'given', 'glass',
    'globe', 'going', 'grace', 'grade', 'grand', 'grant', 'grass', 'great', 'green', 'gross',
    'group', 'grown', 'guard', 'guess', 'guest', 'guide', 'habit', 'happy', 'harry', 'harsh',
    'heart', 'heavy', 'hence', 'henry', 'horse', 'hotel', 'house', 'human', 'ideal', 'image',
    'imply', 'index', 'inner', 'input', 'issue', 'irony', 'joint', 'jones', 'judge', 'juice',
    'known', 'label', 'large', 'laser', 'later', 'laugh', 'layer', 'learn', 'lease', 'least',
    'leave', 'legal', 'level', 'lewis', 'light', 'limit', 'links', 'lives', 'local', 'hello',
    'logic', 'loose', 'lower', 'lucky', 'lunch', 'lying', 'magic', 'major', 'maker', 'march',
    'maria', 'match', 'maybe', 'mayor', 'means', 'meant', 'media', 'metal', 'meter', 'might',
    'minor', 'minus', 'mixed', 'model', 'money', 'month', 'moral', 'motor', 'mount', 'mouse',
    'mouth', 'movie', 'music', 'needs', 'never', 'newly', 'night', 'noise', 'north', 'noted',
    'novel', 'nurse', 'occur', 'ocean', 'offer', 'often', 'onset', 'opera', 'order', 'other',
    'ought', 'outer', 'owner', 'paint', 'panel', 'paper', 'paris', 'party', 'patch', 'pause',
    'peace', 'penny', 'peter', 'phase', 'phone', 'photo', 'piece', 'pilot', 'pitch', 'place',
    'plain', 'plane', 'plant', 'plate', 'point', 'pound', 'power', 'press', 'price', 'pride',
    'prime', 'print', 'prior', 'prize', 'probe', 'promo', 'proof', 'proud', 'prove', 'queen',
    'query', 'quest', 'quick', 'quiet', 'quite', 'quote', 'radio', 'raise', 'rally', 'range',
    'rapid', 'ratio', 'reach', 'react', 'ready', 'realm', 'rebel', 'refer', 'relax', 'shear',
    'reply', 'rhyme', 'right', 'rival', 'river', 'robot', 'rocky', 'roman', 'rough', 'round',
    'route', 'royal', 'rural', 'sadly', 'saint', 'salad', 'salon', 'sandy', 'sauce', 'scale',
    'scare', 'scene', 'scope', 'score', 'sense', 'serve', 'seven', 'shall', 'shame', 'shape',
    'share', 'sharp', 'sheet', 'shelf', 'shell', 'shift', 'shine', 'shirt', 'shock', 'shoot',
    'shore', 'short', 'shout', 'shown', 'sight', 'silly', 'since', 'sixth', 'skill', 'skirt',
    'slave', 'sleep', 'slice', 'slide', 'slope', 'small', 'smart', 'smell', 'smile', 'smoke',
    'solar', 'solid', 'solve', 'sorry', 'sound', 'south', 'space', 'spare', 'speak', 'speed',
    'spend', 'spent', 'split', 'spoke', 'sport', 'staff', 'stage', 'stair', 'stake', 'stand',
    'stare', 'start', 'state', 'steal', 'steam', 'steel', 'steep', 'steer', 'stick', 'hated',
    'stiff', 'still', 'stock', 'stone', 'stood', 'store', 'storm', 'story', 'strap', 'straw',
    'strip', 'stuck', 'study', 'stuff', 'style', 'sugar', 'suite', 'super', 'sweet', 'swing',
    'table', 'taken', 'taste', 'taxes', 'teach', 'teeth', 'tense', 'tenth', 'thank', 'theft',
    'their', 'theme', 'there', 'these', 'thick', 'thing', 'think', 'third', 'those', 'three',
    'throw', 'thumb', 'tight', 'timed', 'timer', 'title', 'today', 'token', 'tooth', 'topic',
    'total', 'touch', 'tough', 'towel', 'tower', 'toxic', 'trace', 'track', 'trade', 'trail',
    'train', 'treat', 'trend', 'trial', 'tribe', 'trick', 'tried', 'troop', 'truce', 'truck',
    'truly', 'trust', 'truth', 'twice', 'twist', 'uncle', 'under', 'undue', 'union', 'unite',
    'until', 'upper', 'upset', 'urban', 'usage', 'usual', 'valid', 'value', 'video', 'virus',
    'visit', 'vital', 'voice', 'voter', 'waste', 'watch', 'water', 'weary', 'weigh', 'weird',
    'whale', 'wheat', 'wheel', 'where', 'which', 'while', 'white', 'whole', 'whose', 'woman',
    'women', 'world', 'worry', 'worse', 'worst', 'worth', 'would', 'wound', 'woven', 'wrist',
    'write', 'wrong', 'wrote', 'yield', 'young', 'youth', 'aback', 'abase', 'abate', 'abbey',
    'abbot', 'abhor', 'abide', 'abled', 'abode', 'abort', 'ached', 'acorn', 'poler', 'mover',
    'adapt', 'added', 'adept', 'adieu', 'adorn', 'afoot', 'afore', 'crane', 'maple',
    'afoul', 'after', 'agape', 'agile', 'aging', 'aglow', 'agony', 'agora', 'agree',
    'ahead', 'aider', 'aisle', 'alarm', 'album', 'alder', 'alert', 'algae', 'alias', 'alibi',
    'alien', 'align', 'alike', 'alive', 'allay', 'alley', 'allot', 'allow', 'alloy', 'aloft',
    'aloha', 'alone', 'along', 'aloof', 'aloud', 'alpha', 'altar', 'alter', 'amass', 'amaze',
    'amber', 'amble', 'amend', 'amiss', 'amity', 'among', 'ample', 'amply', 'amuse', 'angel',
    'anger', 'angle', 'angry', 'angst', 'anime', 'ankle', 'annex', 'annoy', 'annul', 'anode',
    'antic', 'anvil', 'aorta', 'apace', 'apart', 'aphid', 'aping', 'apnea', 'apple', 'apply',
    'apron', 'aptly', 'arbor', 'ardor', 'arena', 'argon', 'argue', 'arise', 'armed', 'armor',
    'aroma', 'arose', 'array', 'arrow', 'arson', 'artsy', 'ascot', 'ashen', 'aside', 'askew',
    'assay', 'asset', 'atoll', 'atone', 'attic', 'audio', 'audit', 'augur', 'aunty', 'aural',
    'avail', 'avers', 'avert', 'avian', 'avoid', 'await', 'awake', 'award', 'aware', 'awash',
    'awful', 'awoke', 'axial', 'axiom', 'axion', 'azure', 'bacon', 'badge', 'badly', 'bagel',
    'baggy', 'baker', 'baler', 'balmy', 'banal', 'banjo', 'barge', 'baron', 'basal', 'basic',
    'basil', 'basin', 'basis', 'baste', 'batch', 'bathe', 'baton', 'batty', 'bawdy', 'bayou',
    'beach', 'beady', 'beard', 'beast', 'beech', 'beefy', 'befit', 'began', 'begat', 'beget',
    'begin', 'begun', 'being', 'belch', 'belie', 'belle', 'belly', 'below', 'bench', 'beret',
    'berry', 'berth', 'beset', 'betel', 'bevel', 'bezel', 'bible', 'bicep', 'biddy', 'bigot',
    'bilge', 'billy', 'binge', 'bingo', 'biome', 'birch', 'birth', 'bison', 'bitty', 'black',
    'blade', 'blame', 'bland', 'blank', 'blare', 'blast', 'blaze', 'bleak', 'bleat', 'bleed',
    'bleep', 'blend', 'bless', 'blimp', 'blind', 'blink', 'bliss', 'blitz', 'bloat', 'block',
    'bloke', 'blond', 'blood', 'bloom', 'blown', 'bluer', 'bluff', 'blunt', 'blurb', 'blurt',
    'blush', 'board', 'boast', 'bobby', 'boney', 'bongo', 'bonus', 'booby', 'boost', 'booth',
    'booty', 'booze', 'boozy', 'borax', 'bored', 'borer', 'borne', 'boron', 'bosom', 'bossy',
    'botch', 'bough', 'boule', 'bound', 'bowel', 'boxer', 'brace', 'braid', 'brain', 'brake',
    'brand', 'brash', 'brass', 'brave', 'bravo', 'brawl', 'brawn', 'bread', 'break', 'breed',
    'briar', 'bribe', 'brick', 'bride', 'brief', 'brine', 'bring', 'brink', 'briny', 'brisk',
    'broad', 'broil', 'broke', 'brood', 'brook', 'broom', 'broth', 'brown', 'brunt', 'brush',
    'brute', 'buddy', 'budge', 'buggy', 'bugle', 'build', 'built', 'bulge', 'bulky', 'bully',
    'bunch', 'bunny', 'burly', 'burnt', 'burst', 'bused', 'bushy', 'butch', 'butte', 'buxom',
    'buyer', 'bylaw', 'cabal', 'cabby', 'cabin', 'cable', 'cacao', 'cache', 'cacti', 'caddy',
    'cadet', 'cagey', 'cairn', 'camel', 'cameo', 'canal', 'candy', 'canny', 'canon', 'caper',
    'caput', 'carat', 'cargo', 'carol', 'carry', 'carve', 'caste', 'catch', 'cater', 'catty'
]
#Different functions for different games
def speed_typing():
    playing = 1 
    global fastest_time_record
    print(f"Welcome to speed typing {name}! \n Just type 10 words which were randomly chosen correctly without capitalisation as fast as you can. \n Fastest time goes to the leaderboard! Starts in 3 seconds. Good luck!")
    time.sleep(5)  #Allows the user to read the instruction by waiting 5 seconds
    while playing:  #Until the user says they want to exit, it keeps looping the game
        sentence = ""
        for i in range(10):
            sentence +=  typing_words_list[random.randint(0,len(typing_words_list))-1] + " "  #Creates a sentence by getting a random word from 1000 words list and adding it 10 times to a blank string
        for i in range(3,0,-1): #Waits 3 seconds before starting
            print(i)
            time.sleep(1)    
        print(f"Type: {sentence}")
        start_time = time.time()
        user_sentence = input("Type: ")
        if user_sentence.strip() == sentence.strip():
            end_time = time.time()
            time_record = round(end_time - start_time,2)  #How fast they typed is calculated by the time the user finished minus time the user started
            print(time_record, "seconds")
            if time_record < fastest_time_record[0]:  #If the user did faster than the fastest record, it becomes the new fastest record.
                fastest_time_record = (time_record,name)
                print(f"New high record! {name} : {time_record} seconds")
        else:
            print("Incorrect sentence.")
        playing = None
        while playing != 0 and playing != 1:  #Until the user inputs to play again or exit, it keeps asking if they want to play again
            try:
                playing = int(input("Do you want to play again? \n 0 : No \n 1 : Yes \n"))
                if playing != 0 and playing != 1:
                    raise ValueError
            except ValueError:
                print("Please try again.")
    return
def wordle():
    playing = 1 
    global highest_wordle_streak
    streak = 0
    #Similar overall structure as speed_typing
    print(f" Welcome to Wordle {name}! \n Guess a random 5 letter english word in 6 tries. Unfortunately, not all words are included. \n If your try contains the correct letter at correct place it will be print GREEN \n Correct letter but at the wrong place YELLOW \n Incorrect letter RED. \n You can keep playing to increase your win streak and highest streak goes in the leaderboard. \n Good luck!")  
    while playing: 
        tries = 6  #The user has 6 guesses of words.
        word = wordle_words_list[random.randint(0,len(wordle_words_list)-1)]  #Gets a random word from the 5 letter word list
        while tries != 0:  #Until the user uses all guesses, it repeats the user to input guess.
            guess_hint = []  
            guess = input("\n Guess : ")
            if guess.lower().strip() in wordle_words_list:  #If the guess is in the possible solutions, it allows the guess.
                tries -= 1
                for i in range(5):  #Goes over the word to check if it is in the right place, in the wrong place, or not at all and appends the according colour in order.
                   if guess.lower()[i] == word[i]:
                       guess_hint.append("GREEN")
                   elif guess.lower()[i] in word:
                       guess_hint.append("YELLOW")
                   else:
                       guess_hint.append("RED")
            else: #If the guess is invalid, it goes back to asking the guess.
                print("Invalid word.")
                continue
            for colours in guess_hint:  #Prints out to the user if what letter is in which state and how many tries they have left.
                print(colours,end = " ")
            print(f"\n{tries} tries left.")
            if guess == word:  #If the user correctly guesses the word, it increases their streak and ends the game.
                print("Correct!")
                streak += 1
                if streak > highest_wordle_streak[0]: 
                    highest_wordle_streak = (streak,name)
                    print(f"New high record! {name} : {streak} correct answers in a row!")
                    tries = 6  #To prevent guessing correctly on the last try printing that you didn't get it, try is reseted to 6.
                    break
        if tries <= 0: #If the game ends without the user guessing it correctly, streak resets and the word is revealed.
            print(f"Unfortunate, the answer was: {word}.")
            streak = 0
        playing = None
        while playing != 0 and playing != 1:
            try:
                playing = int(input("Do you want to play again? (STREAK ENDS IF YOU EXIT) \n 0 : No \n 1 : Yes \n"))
                if playing != 0 and playing != 1:
                    raise ValueError
            except ValueError:
                print("Please try again.")
    return
name = input("What is your name? ")
print(f"Welcome to Games Conpendium, {name}!")
while action != "exit": #Keep taking inputs and allows the user to take the following action. The user can keep playing as much as they want.
    try:
        action = int(input("What do you wish to do? \n 1 : speed typing \n 2 : wordle \n 3 : paper scissors rock \n 4 : leaderboard, \n 5 : exit \n"))
    
        if action == 1:
            speed_typing()
            continue
        elif action == 2:
            wordle()
            continue
        elif action == 3:
            print("play paper scissors rock")
            continue
        elif action == 4:
            print("show leaderboard")
            continue
        elif action == 5:
            print("Thank you for playing!")
            break
        else:
            raise ValueError
    except ValueError: #If action is not any of the options, it asks the user to try again.
        print("Please try again.")
        continue
